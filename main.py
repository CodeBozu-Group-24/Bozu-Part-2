from bs4 import BeautifulSoup
import requests
import csv
from csv import writer
data = requests.get('https://www.politico.com/news/magazine/2021/01/18/trump-presidency-administration-biggest-impact-policy-analysis-451479').text
soup = BeautifulSoup(data, 'lxml')
soupdata1 = soup.findAll('h3', class_='story-text__heading-medium label')
soupdata2 = soup.findAll('h3', class_='story-text__heading-medium')
for elements in soupdata1:
    info = elements.get_text()
    print(info)    
for elements in soupdata2:
    info = elements.get_text()
    print(info)        