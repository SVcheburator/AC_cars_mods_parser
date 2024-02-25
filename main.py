from bs4 import BeautifulSoup
import pandas as pd
import requests

data = {'car_name': [], 'download_link': []}

url = "https://www.assetto-fr.tk/garage/"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

cadre = doc.find(class_ = "cadre")
brand_btns = cadre.find_all('a')

for brand_btn in brand_btns:
    brand = brand_btn.get('href')
    brand_url = f"https://www.assetto-fr.tk/garage/{brand}/"
    page = requests.get(brand_url).text
    doc = BeautifulSoup(page, "html.parser")

    cars = doc.find_all(class_ = "texte_centrer")

    for car in cars:
        car_name = car.get_text().split("*")[0]
        try:
            download_link = car.a['href']
        except TypeError:
            download_link = car.find_all('option')[1]['value']
        
        data['car_name'].append(car_name)
        data['download_link'].append(download_link)

df = pd.DataFrame(data)
df.to_excel('mods.xlsx', index=False)