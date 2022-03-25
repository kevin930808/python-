import requests
from bs4 import BeautifulSoup
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
infos = soup.find('div',{'class':"D(f) Ai(fe) Mb(4px)"}).find_all('span')
for i in infos:
    print(i.text)