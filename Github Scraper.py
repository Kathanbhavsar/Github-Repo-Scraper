from bs4 import BeautifulSoup as soup
import csv
import requests
import json

base_url = "https://github.com"
file=open('Github_top_repo.csv','w')
csv_writer=csv.writer(file)
csv_writer.writerow(["Name of The Repo","Description of the project","Link to the project"])

url = "https://github.com/trending"
url_req = requests.get(url)
url_soup = soup(url_req.text, "html.parser")
content = url_soup.findAll('article', class_='Box-row')
for idx, top in enumerate(content):
    try:
        name = top.h1.a.get_text(strip=True)
        description = top.p.get_text(strip=True)
        link = top.h1.a.attrs['href']
        print(name, description, base_url + link)
        csv_writer.writerow([name, description, base_url + link])
    except Exception as e:
        description=None
file.close()
