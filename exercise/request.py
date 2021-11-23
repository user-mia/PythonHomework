import time
import random
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://movie.douban.com/top250"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
}

params = {'start': 0}

r = requests.get(url, params=params, headers=headers)

# 解析写入excel
soup = BeautifulSoup(r.text, 'lxml')
for i, item in enumerate(soup.find_all(attrs={'class': 'hd'})):
    print(item.a['href'])


# for k,i in enumerate( soup.find_all(attrs={'class': 'bd'})):
#     # 评分
#     # print(i.find_all(name='span', attrs={'property': 'v:average'}))
#
#     # 评价人数
#     if k:
#         # print((i.find_all(name='span', attrs={}))[3])
