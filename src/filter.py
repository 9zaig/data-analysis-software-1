import re
import glob
import os


class filter:
    os.chdir('../dat')
    def __init__(self, lot_id, wafer_id, device_name, xy_cord, BASEPATH = os.getcwd()):
        self.lot_id = lot_id
        self.wafer_id = wafer_id
        self.device_name = device_name
        self.xy_cord = xy_cord
        self.BASEPATH = BASEPATH

    def find_xy_cord(self, files, xy_cords):
        if len(xy_cords) == 0:
            return files
        else:
            result = []
            for f in files:
                for xy in xy_cords:
                    if xy in f:
                        result.append(f)
            return result

    def process_path(self, path):
        if len(path) == 0:
            path = list()
            path.append('*')
        return path

    def filter(self):
        path_lot = self.process_path(self.lot_id)
        path_wafer = self.process_path(self.wafer_id)
        if len(self.device_name) == 3:
            regex = re.compile('{}\\w.xml'.format(self.device_name))
        else:
            regex = re.compile('{}.xml'.format(self.device_name))

        result = list()
        for lot in path_lot:
            dir_path = self.BASEPATH + lot
            for wafer in path_wafer:
                file_path = dir_path + '/{}/**/*.xml'.format(wafer)
                fileList = glob.glob(file_path, recursive=True)
                for f in fileList:
                    file = os.path.realpath(f)
                    if re.search(regex, file) != None:
                        result.append(os.path.realpath(file))

        return self.find_xy_cord(result, self.xy_cord)

# input value is not accepted by filter.py
lot_id = list(map(str, input('lot_id : ').split()))
wafer_id = list(map(str, input('wafer_id : ').split()))

while 1 :
    device_name = input('device_name : ')
    if device_name == 'LMZ' :
        break
    else :
        print('TRY AGAIN')
        continue

xy_cord = list(map(str, input('xy_cord : ').split()))

f = filter(lot_id, wafer_id, device_name, xy_cord)
r = f.filter()
print(r)

