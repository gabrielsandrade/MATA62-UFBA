import pandas as pd
from settings import *
from scrape import *
import matplotlib.pyplot as plt


def main():
    #scrapePage(anacUrl)

    # Realizar tratamento de dados
    voos = []
    for i in range(1, 13):
        print('Calculando quantidade de voos em 2019, mês : ', i)
        sep = [';', ',','\t']
        sepIndex = 0
        while True:
            try:
                fileCsv = pd.read_csv(
                    f'data/2019-{i:02}.csv', encoding='ISO-8859-1', sep=sep[sepIndex])
                if ('internet' in fileCsv.columns[0]):
                    fileCsv.columns = fileCsv.iloc[0]
                    fileCsv = fileCsv[1:]
                if len(fileCsv.columns) <= 1:
                    raise ValueError('sepIndex')
                else:
                    try:
                        fileCsv = fileCsv.drop(columns='Data Prevista')
                    except:
                        pass
                    fileCsv.columns = ['ICAO Empresa Aérea', 'Número Voo', 'Código DI', 'Código Tipo Linha',
                                       'ICAO Aeródromo Origem', 'ICAO Aeródromo Destino', 'Partida Prevista',
                                       'Partida Real', 'Chegada Prevista', 'Chegada Real', 'Situação Voo',
                                       'Código Justificativa']
                situacao = fileCsv['Situação Voo']
                voos.append(situacao.value_counts())
                break
            except Exception as e:
                if e.args[0] == 'sepIndex':
                    if (sepIndex < 3):
                        sepIndex += 1
                else:
                    print(e)
        
        print (voos[i - 1])


if __name__ == "__main__":
    main()
