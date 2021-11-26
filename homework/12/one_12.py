"""
中文电影名和外文电影名
SWE19033 hwx
"""
import re
from homework import getHtml

URL = "https://movie.douban.com/top250"
pat = re.compile(r'<span class="title">(.*)</span>\s*<span class="title">&nbsp;/&nbsp;(.*)</span>')

for start in range(0, 250, 25):
    text = getHtml.get_html_text(url=URL, params={'start': start})
    for item in pat.findall(text):
        print(f'{item[0]:<20}  {item[1]:<40}')
