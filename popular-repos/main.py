from bs4 import BeautifulSoup
import pandas
import requests

url="https://github.com/collections"

page=requests.get(url)
soap=BeautifulSoup(page.content,'html.parser')

titles=soap.find_all('h2',class_='h3')
title=[]
for t in titles:
    title.append(t.text)

my_dict={'repo':title}

dataframe=pandas.DataFrame(my_dict)
dataframe.to_excel('populer-repos-name.xlsx')