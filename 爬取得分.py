import csv
import requests

url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=1000'
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)",
    "referer": "https://movie.douban.com/typerank"
}
response = requests.get(url=url, headers=headers)
data = response.json()
print(data)

with open('score.csv', 'w', newline='', encoding='utf-8') as fp:
    writer = csv.writer(fp)

    writer.writerow(['imgid', 'score'])

    for i in data:
        cover_url = i['cover_url']
        score = i['score']
        imgid = cover_url.split('/')[-1]
        id = url.split('/')[-2]

        row_data = [imgid]
        row_data.append(score)

        writer.writerow(row_data)
        print(i)
