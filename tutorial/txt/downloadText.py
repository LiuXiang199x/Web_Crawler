# 网路爬虫，一般爬取的东西无非也就四种：文字、图片、音乐、视频。
# https://cuijiahua.com/blog/2020/04/spider-7.html
# 爬虫其实很简单，可以大致分为三个步骤：
#    发起请求：我们需要先明确如何发起 HTTP 请求，获取到数据。
#    解析数据：获取到的数据乱七八糟的，我们需要提取出我们想要的数据。
#    保存数据：将我们想要的数据，保存下载。
# 发起请求，我们就用 requests 就行，上篇文章已经介绍过。
# 解析数据工具有很多，比如xpath、Beautiful Soup、正则表达式等。本文就用一个简单的经典小工具，Beautiful Soup来解析数据。
# 保存数据，就是常规的文本保存。

from matplotlib.pyplot import text
import requests
from bs4 import BeautifulSoup


target = 'https://www.biqupai.com/15_15338/8549128.html'
chapter_url = "https://www.biqupai.com/15_15338/"
server = "https://www.biqupai.com"



def first_paso(target_):
    
    print("============ 从URL中获取HTML信息 =========")
    req = requests.get(url = target_)
    req.encoding = 'utf-8'
    print(req.text)
    print("=========== Get HTML done ===========\n")

    return req.text


def second_paso(txts):
    print("========= 开始解析数据(Beautiful Soup) ==========")
    print("======== 提取原始数据 ========")
    bs = BeautifulSoup(txts, "lxml")
    texts = bs.find("div", id="wrapper")
    texts = texts.find("div", {"content_read"})
    texts = texts.find("div", id="content")

    print("======== 原始数据提取Done ========")
    print("======== 清晰原始数据 ========")
    #  strip 方法去掉回车，最后使用 split 方法根据 \xa0 切分数据，因为每一段的开头，都有四个空格。
    texts = texts.text.strip().split("\xa0"*4)
    print("======== 一个章节数据清晰完毕 ========")
    print("======== 开始处理所有章节数据 ========")
    
    chapter_url = "https://www.biqupai.com/15_15338/"
    ch_req = requests.get(url = chapter_url)
    ch_req.encoding = "utf-8"
    chapters_bs = BeautifulSoup(ch_req.text, "lxml")
    chapters = chapters_bs.find("div", id="wrapper")
    chapters = chapters.find_all("div", {"box_con"})[1]
    print(type(chapters))
    print(len(chapters))
    chapters = chapters.find("div", id="list")
    # chapters.find_all('a') 就是在找到的 div 标签里，再提取出所有 a 标签
    chapters = chapters.find_all("a")
    
    for item in chapters:
        print(item)
        url = item.get("href")
        print(item.string)
        print(server+url)
    
    return texts

if __name__ == '__main__':
    htmll = first_paso(target)
    bss = second_paso(htmll)
    # print(bss)