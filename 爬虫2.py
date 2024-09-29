import requests
from lxml import etree
import re
import pickle

def parse(response):
    pattern = re.compile(r'\r\n|\u2003|\xa0',re.S)
    response.encoding = response.apparent_encoding
    text = response.text
    html = etree.HTML(text)

    div = html.xpath('//div[@class="v_news_content"]//text()')
    content_list =[s for s in div if not pattern.match(s)]
    news_content = ' '.join([s for s in content_list])
    pnext = html.xpath('//div[@class="pnext"]//a//@href')
    if len(pnext) == 1:
        next_page = pnext[0]
    else:
        next_page = pnext[1]
    return news_content, next_page

news_corpus=[]
headers = {
    'Referer':'http://news.xjtu.edu.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
}

response_start = requests.get('http://news.xjtu.edu.cn/info/1033/209597.htm', headers=headers)
news_content,next_page=parse(response_start)
news_corpus.append(news_content)

for i in range(99):
    response = requests.get('http://news.xjtu.edu.cn/info/1033/'+next_page, headers=headers)
    news_content, next_page = parse(response)
    news_corpus.append(news_content)
#
print(news_corpus)
print('=' * 50)
with open('news_corpus.pkl', 'wb') as f:
    pickle.dump(news_corpus, f)