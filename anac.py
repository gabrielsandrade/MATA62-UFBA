from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup as bs
import pandas as pd
from settings import *
import  zipfile, io, requests, wget, os

url = 'https://www.anac.gov.br/assuntos/dados-e-estatisticas/historico-de-voos'

def scrapeYear(year, yearTitle):
    firstRow = (year.next_sibling.next_sibling)
    firstRowLinks = firstRow.find_all('a')
    secondRow = firstRow.next_sibling.next_sibling
    secondRowLinks = secondRow.find_all('a')
    fileLinks = firstRowLinks + secondRowLinks
    path = os.path.join('data')
    if not os.path.exists(path):
        os.makedirs(path)
    for index, link in enumerate(fileLinks) :
        try:
            if yearTitle in link['href'] : 
                extension = link['href'].split('.')[-1]
                fileName = f"{yearTitle}-{index + 1:02}.{extension}"
                print(fileName)
                filePath = os.path.join(path, fileName)
                if not os.path.exists(filePath):
                    wget.download(link['href'], out=filePath)
                else : print("Arquivo já foi baixado anteriorment.")
        except :
            pass

def main () :
    response = urlopen(url)
    anacSite = bs(response.read(), 'lxml')
    table = anacSite.find(class_='plain')
    years = table.find_all('tr')
    for year in years :
        yearTitle = year.find('h2')
        try:
            if int(yearTitle.text) in range(2015, 2020):
                print (yearTitle.text)
                scrapeYear(year, yearTitle.text)
        except:
            pass

if __name__ == "__main__":
    main()