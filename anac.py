import pandas as pd
from settings import *
from scrape import *
import matplotlib.pyplot as plt


def main():
    # scrapePage(anacUrl)

    # Realizar tratamento de dados
    voos = []


fileCsv = [[], [], [], [], []]
for z in range(2015, 2020):
    ano = z - 2015
    print(z, ano)
    for i in range(1, 13):
        print('Quantidade de voos em 2019, mês : ', i)
        sep = [';', ',', '\t']
        sepIndex = 0
        while True:
            try:
                fileCsv[ano] = pd.read_csv(
                    f'data/{z}-{i:02}.csv', encoding='ISO-8859-1', sep=sep[sepIndex], low_memory=False)
                if ('internet' in fileCsv[ano].columns[0]):
                    fileCsv[anos].columns = fileCsv[ano].iloc[0]
                    fileCsv[anos] = fileCsv[ano][1:]
                if len(fileCsv[ano].columns) <= 1:
                    raise ValueError('sepIndex')
                else:
                    try:
                        fileCsv[ano] = fileCsv[ano].drop(
                            columns='Data Prevista')
                    except:
                        pass
                    fileCsv[ano].columns = ['ICAO Empresa Aérea', 'Número Voo', 'Código DI', 'Código Tipo Linha',
                                            'ICAO Aeródromo Origem', 'ICAO Aeródromo Destino', 'Partida Prevista',
                                            'Partida Real', 'Chegada Prevista', 'Chegada Real', 'Situação Voo',
                                            'Código Justificativa']
                situacao = fileCsv[ano]['Situação Voo']
                voos.append(situacao.value_counts())
                break
            except Exception as e:
                if e.args[0] == 'sepIndex':
                    if (sepIndex < 3):
                        sepIndex += 1
                else:
                    print(e)


if __name__ == "__main__":
    main()
