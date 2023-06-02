
import requests

from bs4 import BeautifulSoup

url = 'https://zh.wikipedia.org/wiki/Python'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 获取标题
    title = soup.title.string
    print(f"Python编程语言：{title}")
    
    # 获取摘要
    summary = soup.find('div', {'class': 'reflist'}).previous_sibling.previous_sibling.text
    print(f"简介：{summary}")
else:

    print(f"请求失败，状态码：{response.status_code}")

