from bs4 import BeautifulSoup
import requests

characters = [
    ("1086", "Sousuke_Aizen"),
    ("128909", "Kiyotaka_Ayanokouji"),
    ("164471", "Satoru_Gojou"),
    ("171572", "Cid_Kagenou"),
    ("30", "Gon_Freecss"),
    ("80", "Light_Yagami"),
    ("175198", "Sukuna_Ryoumen"),
]

directory = "datasets/"
main_website = "https://myanimelist.net/character/pics"

character = characters[0]
# for character in characters:
website = main_website.split("/")
website[-3:-1] += character
url = "/".join(website)
r = requests.get(url).text
soup = BeautifulSoup(r, 'lxml')
table = soup.find('h2', class_='mb8').parent
img_tab = table.find('table').tbody
print(img_tab)
