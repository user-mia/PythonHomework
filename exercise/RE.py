"""
正则表达式
SWE19033 hwx
"""
import re

# 模式 - 座机电话
pat = re.compile(r'\d{3}-\d{8}|\d{4}-\d{7,8}')

# match search finditer findall split sub

html_doc = 'Home Tel:021-26778981, school Tel:0596-2182932'
# 只匹配一个
# mat = pat.search()
# 从最开始匹配
# mat =  pat.match()
# 返回一个迭代器
# mat = pat.finditer(html_doc)
# 返回一个结果的列表
# mat = pat.findall(html_doc)
# 返回分割后的列表
# mat = pat.split(html_doc)
# 饭后替换后的字符串
# mat = pat.sub('替换', html_doc)

# pat2 = re.compile(r'\s|: \d{2,3}')
# text = """
# Pi = 3.
# 1415926535 1415926535 1415926535 1415926535 1415926535 : 50
# 1415926535 1415926535 1415926535 1415926535 1415926535 : 100
# """


text = 'Cats arethan dogs'
pat2 = re.compile(r'(.*) are.*?than (.*)')
mat = pat2.match(text)
print(mat)
# if mat:
#     print(mat.group(0))
#     print(mat.group(1))
#     print(mat.group(2))
# else:
#     print("no answer~")

# 默认 贪婪匹配和最小匹配
# 最短匹配字符串 加 *？，+？，？？，{m,n}?
