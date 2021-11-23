from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')


# print(soup.prettify())
# print(soup.find_all('a'))


def search(tag):
    return tag.name == 'a'


first = soup.find_all(lambda x: x.name == 'a')
third = soup.find_all(lambda x: x['class'] == 'sister' and x['id'] == 'link3')

for i in first:
    print(f"标签文本：{i.string}, 链接：{i['href']}")

print(third)
