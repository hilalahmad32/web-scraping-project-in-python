from random import random
from bs4 import BeautifulSoup
import pandas
import requests
from datetime import datetime
to_date=datetime.today().strftime("%Y-%m-%d")

url="https://www.brainyquote.com/authors/friedrich-nietzsche-quotes"
page=requests.get(url)
soap=BeautifulSoup(page.content,'html.parser')
qoutes=soap.find_all('a',class_="b-qt")
qoute=[]
for q in qoutes:
    qoute.append(q.text.strip())
my_dict={'qoutes':qoute}
dataframe=pandas.DataFrame(my_dict)
dataframe.to_excel(f'qoutes-{to_date}-3.xlsx')