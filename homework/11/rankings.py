"""
第 11 周 爬取大学排名
SWE19033 hwx
"""

import time
import random
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

URL = "https://www.shanghairanking.cn/rankings/bcur/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
}

excel = Workbook()

for year in range(2017, 2022):
    print(f'爬取 {year} 年数据')
    time.sleep(random.randint(1, 3))

    r = requests.get(f'{URL}{year}', headers=headers)
    r.encoding = 'utf-8'

    # 新建sheet 插入第一个位置
    ws = excel.create_sheet(str(year), 0)
    ws.append(['排名', '学校名称', '省市', '类型', '总分', '详情链接'])

    # html 解析
    soup = BeautifulSoup(r.text, 'lxml')
    # 获取全部学校 名称 其中包含链接
    name_and_href = [(i.string, 'https://www.shanghairanking.cn' + i.attrs['href'])
                     for i in soup.find_all(attrs={'class': 'name-cn'})]

    # 获取全部学校，并 去除 标题行
    for i, item in enumerate((soup.find_all(name='tr'))[1:]):
        # 省市
        temp = item.contents[2]
        location = temp.contents[0].strip()

        # 类型
        temp1 = item.contents[3]
        school_type = temp1.contents[0].strip()

        # 分数
        temp2 = item.contents[4]
        score = temp2.string.strip()

        # 写入Excel 表
        # print([i, name_and_href[i][0], location, school_type, score, name_and_href[i][1]])
        ws.append([i + 1, name_and_href[i][0], location, school_type, score, name_and_href[i][1]])

    # 设置列宽
    ws.column_dimensions['B'].width = 20
    ws.column_dimensions['F'].width = 90

# 保存
excel.save('中国最好的大学.xlsx')
excel.close()
# 提示完成
print('success!')
