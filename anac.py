import pandas as pd
from settings import *
from scrape import *


def main():
    # scrapePage(anacUrl)

    # Realizar tratamento de dados
    for i in range(1, 13):
        print('Quantidade de voos em 2019, mês : ', i)
        sep = [',', ';', '\t']
        sepIndex = 0
        while True:
            try:
                fileCsv = pd.read_csv(
                    f'data/2019-{i:02}.csv', encoding='ISO-8859-1', sep=sep[sepIndex])
                if len(fileCsv.columns) <= 1:
                    raise ValueError('sepIndex')
                else:
                    fileCsv.columns = ['ICAO Empresa Aérea', 'Número Voo', 'Código DI', 'Código Tipo Linha',
                                       'ICAO Aeródromo Origem', 'ICAO Aeródromo Destino', 'Partida Prevista',
                                       'Partida Real', 'Chegada Prevista', 'Chegada Real', 'Situação Voo',
                                       'Código Justificativa']
                situacao = fileCsv['Situação Voo']
                print(situacao.value_counts())
                break
            except Exception as e:
                if e.args[0] == 'sepIndex':
                    if (sepIndex < 3):
                        sepIndex += 1
                else:
                    print(e)


if __name__ == "__main__":
    main()
