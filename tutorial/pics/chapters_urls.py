import requests
from bs4 import BeautifulSoup
 
target_url = "https://www.dmzj.com/info/yaoshenji.html"
r = requests.get(url=target_url)
bs = BeautifulSoup(r.text, 'lxml')
list_con_li = bs.find('ul', class_="list_con_li autoHeight")
comic_list = list_con_li.find_all('a')
chapter_names = []
chapter_urls = []
for comic in comic_list:
    href = comic.get('href')
    name = comic.text
    chapter_names.insert(0, name)
    chapter_urls.insert(0, href)
 
# 打开第一章的链接，你会发现，链接后面自动添加了#@page=1。
# 你翻页会发现，第二页的链接是后面加了#@page=2，第三页的链接是后面加了#@page=3，以此类推。


print(chapter_names)
print(chapter_urls)