import requests
from bs4 import BeautifulSoup

url="https://www.themoviedb.org/movie"
page=requests.get(url)
soap=BeautifulSoup(page.content,'html.parser')
titles=soap.find_all('h2')
for t in titles:
    print(t)

# he block the request