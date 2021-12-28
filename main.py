from bs4 import BeautifulSoup
import requests
import csv
from csv import writer
data = requests.get('https://www.politico.com/news/magazine/2021/01/18/trump-presidency-administration-biggest-impact-policy-analysis-451479').text
soup = BeautifulSoup(data, 'lxml')
soupdata = soup.findAll('h3', class_='story-text__heading-medium')
for elements in soupdata:
    info = elements.get_text()  #work done names
    print(info)
print("-----------------------------------------------------------------------")
soupMoves = soup.findAll('p', class_="story-text__paragraph")
moves = []
impact = []
upshot = []
count = 1
for element in soupMoves:
    if count == 1:
        moves.append(element)
    elif count == 2:
        impact.append(element)
    elif count ==3:
        upshot.append(element)
    count +=1
    if count > 3:
        count = 1

AllTopics = zip(soupdata, moves, impact, upshot)
