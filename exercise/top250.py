"""
豆瓣 top 250
"""
import time
import random
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

URL = "https://movie.douban.com/top250"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
}

params = {'start': 0}

excel = Workbook()
ws = excel.active

ws.append(['名次', '名称', '链接', '评分', '评价人数'])
for start in range(0, 26, 25):
# for start in range(0, 250, 25):
    # 结果数组
    inputItem = []
    time.sleep(random.randint(1, 3))
    # 提示
    print(f'正在爬取 第 {start // 25 + 1} 页')
    params['start'] = start
    r = requests.get(URL, params=params, headers=headers)

    # 解析写入excel
    soup = BeautifulSoup(r.text, 'lxml')
    for index, item in enumerate(soup.find_all(attrs={'class': 'hd'})):
        # 排名 名称 链接
        inputItem.append([start + index + 1, item.span.string, item.a['href']])

    for index, item in enumerate(soup.find_all(attrs={'class': 'bd'})[1:]):
        # 评分
        inputItem[index].append((item.find_all(attrs={'property': 'v:average'}))[0].string)
        # print(i.find_all(name='span', attrs={'property': 'v:average'}))

        # 评价人数
        inputItem[index].append((item.find_all(name='span'))[3].string)
        # print((i.find_all(name='span', attrs={}))[3])

    # 写入Excel
    for i in inputItem:
        # print(i)
        ws.append(i)

# 设置列宽
ws.column_dimensions['B'].width = 30
ws.column_dimensions['C'].width = 60
ws.column_dimensions['E'].width = 30
# 保存
excel.save('豆瓣top250.xlsx')
excel.close()
# 提示完成
print('success!')
