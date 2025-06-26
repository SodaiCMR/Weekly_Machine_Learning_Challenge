from bs4 import BeautifulSoup
import requests
import os
import time

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
for character in characters:
    website = main_website.split("/")
    website[-3:-1] += character
    url = "/".join(website)
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')
    table = soup.find('h2', class_='mb8').parent.table
    img_table = table.find_all('a', class_="js-picture-gallery")
    for img_cell in img_table:
        img_src = img_cell['href']
        img_desc = img_src.split('/')[-1]
        image_saved = requests.get(img_src)
        if image_saved.status_code != 200:
            print(f"error downloading {img_desc}")
        else:
            character_directory = os.path.join(directory, character[-1])
            if not os.path.exists(character_directory):
                os.makedirs(character_directory)
            img_path = os.path.join(character_directory, img_desc)
            with open(img_path, 'wb') as img_file:
                img_file.write(image_saved.content)
            print(f"Successfully downloaded {img_desc}")
            time.sleep(5) # wait 5 seconds
        time.sleep(10)