import zipfile
import os


def unzip(path, fileName):
    file = zipfile.ZipFile(path, "r")
    for info in file.infolist():
        ext = info.filename.split('.')[1]
        info.filename = os.path.join(
            'data', fileName.split('.')[0] + '.' + ext)
        file.extract(info)
        file.close()
