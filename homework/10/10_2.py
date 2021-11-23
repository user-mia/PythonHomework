import random
import requests
import time

url = 'https://search.jd.com/Search'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
}
params = {
    'keyword': '手机',
    'page': 1
}
# response = requests
for i in range(1, 11):
    params['page'] = i
    response = requests.get(url, headers=headers, params=params)
    print(response.url)
    time.sleep(random.randint(1, 3))

# response.encoding = response.apparent_encoding
print(response.text[:1001])
