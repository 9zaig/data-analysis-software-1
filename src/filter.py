import os
import glob
import re


input_iot = list(map(str, input('lot_id : ').split()))
if len(input_iot) == 0 :
    path_iot = []
    path_iot.append('*')
elif len(input_iot) != 0 :
    path_iot = input_iot

input_wafer = list(map(str, input('wafer_id : ').split()))
if len(input_wafer) == 0 :
    path_wafer = []
    path_wafer.append('*')
elif len(input_wafer) != 0 :
    path_wafer = input_wafer


f_type = list(map(str, input('device_name : ').split()))


regex = re.compile('{}'.format(f_type) + '.xml')
result = list()
for i in path_iot :
    dir_path1 = 'C:/Users/SAMSUNG/Desktop/' + '{}'.format(i)
    for j in path_wafer :
        dir_path2 = dir_path1 + '/{}'.format(j) +  '/**/*.xml'
        fileList = glob.glob(dir_path2, recursive = True)
        for f in fileList :
            file = os.path.realpath(f)
            if re.search(regex, file) != None :
                result.append(os.path.realpath(file))
print(result)

input_xy = list(map(str, input('xy_cord : ').split()))
print(input_xy)
final = []
if len(input_xy) == 0 :
    final = result
else :
    for x in result :
        for i in range(len(input_xy)) :
            if '{}'.format(input_xy[i]) in x :
                final.append(x)

print(final)


