import os
import zipfile
import pandas as pd


def unzip(path, fileName):
    print ("Extraindo arquivo ZIP")
    file = zipfile.ZipFile(path, "r")
    for info in file.infolist():
        ext = info.filename.split('.')[1]
        info.filename = os.path.join(
            'data', fileName.split('.')[0] + '.' + ext)
        file.extract(info)
        file.close()

def convertToCsv(filepath, fileName):
    print ("Convertendo arquivo Excel")
    # wb = pd.ExcelFile(filepath)
    # wb = wb.parse(sheetname=wb.sheet_names[0], index_col=None, na_values=['NA'])
    # newFileName = os.path.join(
    #         'data', fileName.split('.')[0] + '.' + 'csv')
    # wb.to_csv(newFileName, index=False)

    teste = pd.read_excel(filepath)
    teste['Partida Prevista'] = teste['Partida Prevista'].dt.strftime('%d/%m/%Y %H:%M')
    teste['Partida Real'] = teste['Partida Real'].dt.strftime('%d/%m/%Y %H:%M')
    newFileName = os.path.join(
            'data', fileName.split('.')[0] + '.' + 'csv')
    teste.to_csv(newFileName, index=False)
    teste.to_csv(newFileName, index=False)