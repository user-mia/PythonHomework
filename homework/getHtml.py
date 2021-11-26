"""
请求封装
"""
import requests


def get_html_text(url, params=None):
    if params is None:
        params = {}
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'
        }
        r = requests.get(url=url, headers=headers, params=params)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'request fail ~ '
