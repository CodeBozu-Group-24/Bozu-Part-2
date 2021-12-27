from bs4 import BeautifulSoup
import requests
import csv
from csv import writer
data = requests.get('https://www.politico.com/news/magazine/2021/01/18/trump-presidency-administration-biggest-impact-policy-analysis-451479').text
soup = BeautifulSoup(data, 'lxml')
soupdata = soup.findAll('h3', class_='story-text__heading-medium')
for elements in soupdata:
    info = elements.get_text()  #work done names

soupdata2 = soup.findAll('div', class_='story-text')
print(soupdata2)
