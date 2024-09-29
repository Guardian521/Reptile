import requests
import json

url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'
headers = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",
    "referer": "https://movie.douban.com/typerank"
}
response = requests.get(url=url, headers=headers)
data = response.json()
print(data)

for item in data:
    cover_url = item['cover_url']
    imgdata = requests.get(url=cover_url, headers=headers, verify=False).content
    imgname = cover_url.split('/')[-1]
    imgpath = './douban/' + imgname
    with open(imgpath, 'wb') as fp:
        fp.write(imgdata)
        print(imgname, 'chenggong')
