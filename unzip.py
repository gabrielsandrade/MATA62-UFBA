from pathlib import Path
import zipfile
import os

dataPath = 'data'

def unzip(path):
    file = zipfile.ZipFile(path, "r")
    for info in file.infolist():
        print (info.filename)
        for name in file.namelist():
        #salva a extensão do arquivo
            ext = os.path.splitext(name)[1]
        file.extractall(dataPath)
        #renomeia arquivo extraido de acordo com o nome do arquivo zip
        os.rename(dataPath+'/'+name, dataPath+'/'+path.stem+ext)
        file.close()
 

def list_dir(dir):
    #busca o endereço de cada arquivo zip
    for pathzip in list(dir.glob('*.zip')):
        unzip(pathzip)
    print ("Arquivos extraídos")
 

if __name__ == "__main__":
    dir = Path(dataPath)
    list_dir(dir)