import requests

url = 'https://search.dangdang.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
}
params = {
    'key': 'python爬虫',
    'page_index': 0
}
response = requests.get(url, headers=headers, params=params)
response.encoding = response.apparent_encoding
print(response.text)
