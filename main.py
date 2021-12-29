from bs4 import BeautifulSoup
import requests
import csv
from csv import writer
data = requests.get('https://www.politico.com/news/magazine/2021/01/18/trump-presidency-administration-biggest-impact-policy-analysis-451479').text
soup = BeautifulSoup(data, 'lxml')
soupdata = soup.findAll('h3', class_='story-text__heading-medium')
things = []
for elements in soupdata:
    info = elements.get_text()
    things.append(info)  #work done names

things.remove("Religion in schools")

moves = []
impact = []
upshot = []
story_text = soup.find_all("div", {"class":"story-text"})
story_text = story_text[2:]
for story in story_text:
    if "The move" not in story.get_text() or "The impact" not in story.get_text() or "The upshot" not in story.get_text():
        pass
    else:
        storyparagraphs = story.find_all('p', {"class":"story-text__paragraph"})
        for element in storyparagraphs:
            if 'The move:' in str(element):
                moves.append(element.get_text())
            if 'The impact:' in str(element):
                impact.append(element.get_text())
            if 'The upshot:' in str(element):
                upshot.append(element.get_text())

things.append("Religion in schools")
moves.append("DeVos tweaked a wide range of federal education policies, large and small, to bolster faith-based organizations. She changed regulations, for example, to make it easier for members of religious orders to access federal financial aid and expanded federal Public Service Loan Forgiveness to cover clergy members. And she created new protections for faith-based campus organizations at public universities. At the K-12 education level, DeVos stopped enforcing a policy that had prohibited religious organizations from providing publicly funded services—such as tutoring, technology and counseling—in private schools. And she opened up federal grants for charter schools to religiously affiliated organizations.")
impact.append("Many religious education groups praised DeVos’ changes, which she often described as effort to expand religious liberty. “Too many misinterpret the ‘separation of church and state’ as an invitation for government to separate people from their faith,” she said.")
upshot.append("The Biden administration is expected to move quickly to roll back many of DeVos’ education policies, but it’s not yet clear how the incoming administration will approach her various policy tweaks to promote religious organizations.")
for i in range(len(things)):
    full_details = []
    full_details.append(things[i])
    full_details.append(moves[i])
    full_details.append(impact[i])
    full_details.append(upshot[i])
    with open('details.csv', 'a') as f:
        writer_object = writer(f)
        writer_object.writerow(full_details)
        f.close()



