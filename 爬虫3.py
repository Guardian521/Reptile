import requests
import pandas as pd
from bs4 import BeautifulSoup

headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
url='https://www.mafengwo.cn/hotel/40061.html?iMddid=10065#checkin=2024-05-14&checkout=2024-05-16&guests=2-0'
res=requests.get(url, headers=headers).text
print(res)
soup=BeautifulSoup(res, 'html.parser')
print(soup)
score=soup.find_all('div',class_='comm-meta')
comment=soup.find_all('div',class_='txt')

for i in range(len(score)):
    print(score[i])
    print(comment[i].text)
