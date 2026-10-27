import requests
from bs4 import BeautifulSoup

url = "https://fr.wikipedia.org/wiki/Liste_des_éléments_chimiques"
headers = {
    "User-Agent": "MiniProjetChimie/0.1 (projet pedagogique; https://github.com/abmalika1806-spec/mini-projet-chimie)"
}
page = requests.get(url, headers=headers, timeout=20)
print(page.status_code)


soup = BeautifulSoup(page.content, "html.parser")
print(soup.title.get_text())

tableau = soup.find("table", class_="wikitable")
print(tableau.get_text(" ", strip=True)[:500])
