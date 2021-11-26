"""
学校官网通知的前10页内容，包含通知时间，通知链接，通知主题。
SWE19033 hwx
"""
import re
from homework import getHtml

URL = "http://www.xujc.com/index.php?c=Article&a=list&id=151"
pat = re.compile(r'<img .*">\((.*)\)<a href="(.*)" .*>(.*)</a>')
text = getHtml.get_html_text(url=URL)
for i in pat.findall(text):
    href = URL + i[1] if i[1][0] != 'h' else i[1]
    print(i[0], href, i[2])
