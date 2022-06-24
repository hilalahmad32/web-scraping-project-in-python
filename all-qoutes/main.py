from bs4 import BeautifulSoup
import pandas
import requests

title=[]
author=[]
for i in range(1,10+1):
    url=f"https://quotes.toscrape.com/page/{i}/"
    page=requests.get(url)
    soap=BeautifulSoup(page.content,'html.parser')
    titles=soap.find_all('span',class_='text')
    authors=soap.find_all('small',class_='author')
    for i in titles:
        title.append(i.text)
    for a in authors:
        author.append(a.text)

my_dict={'author':author,'qoutes':title}
dataframe=pandas.DataFrame(my_dict)
dataframe.to_excel('all-qoutes.xlsx')