import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
url = "https://www.amazon.in/gp/bestsellers/books/"
page = requests.get(url)

soap = BeautifulSoup(page.content, 'html.parser')
ids = soap.find_all('span', class_='zg-bdg-text')
images = soap.find_all('img', class_='a-dynamic-image')
titles = soap.find_all('div', class_='_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y')
id=[]
image=[]
title=[]
for id1 in ids:
    id.append(id1.text)

for img in images:
    image.append(img.get('src'))

for title1 in titles:
    title.append(title1.text)


my_dict={'id':id,'title':title,'image':image}
dataframe=pd.DataFrame(my_dict)
dataframe.to_excel('index12.xlsx')
        