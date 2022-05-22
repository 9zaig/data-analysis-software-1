import os
import glob
import re

# input value should be input like this.
lot_id = list(map(str, input('lot_id : ').split()))
wafer_id = list(map(str, input('wafer_id : ').split()))
device_name = input('device_name : ')
xy_cord = list(map(str, input('xy_cord : ').split()))


def filter(lot_id, wafer_id, xy_cord, device_name):
    if len(lot_id) == 0:
        path_lot = []
        path_lot.append('*')
    elif len(lot_id) != 0:
        path_lot = lot_id

    if len(wafer_id) == 0:
        path_wafer = []
        path_wafer.append('*')
    elif len(wafer_id) != 0:
        path_wafer = wafer_id

    regex = re.compile('{}.xml'.format(device_name))

    result = list()
    for i in path_lot :
        dir_path1 = 'C:/Users/SAMSUNG/Desktop/' + '{}'.format(i)
        for j in path_wafer :
            dir_path2 = dir_path1 + '/{}'.format(j) +  '/**/*.xml'
            fileList = glob.glob(dir_path2, recursive = True)
            for f in fileList :
                file = os.path.realpath(f)
                if re.search(regex, file) != None :
                    result.append(os.path.realpath(file))

    final = []
    if len(xy_cord) == 0:
        final = result
    else:
        for x in result:
            for i in xy_cord:
                if i in x:
                    final.append(x)
    return final
