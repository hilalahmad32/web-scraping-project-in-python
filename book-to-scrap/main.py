from bs4 import BeautifulSoup
import pandas
import requests

url="http://books.toscrape.com/"
page=requests.get(url)

soap=BeautifulSoup(page.content,'html.parser')
images=soap.find_all('img',class_="thumbnail")
titles=soap.find_all('h3')
prices=soap.find_all('p',class_='price_color')
title=[]
price=[]
image=[]
for img in images:
    image.append(f"http://books.toscrape.com/{img.get('src')}")

for t in titles:
    title.append(t.text)

for p in prices:
    price.append(p.text)

my_dict={'title':title,'price':price,'image':image}
dataframe=pandas.DataFrame(my_dict)
dataframe.to_excel('books.xlsx')