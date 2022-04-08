
from matplotlib.pyplot import text
import requests
from bs4 import BeautifulSoup


target = 'https://www.biqupai.com/15_15338/8549128.html'
chapter_url = "https://www.biqupai.com/15_15338/"

if __name__ == "__main__":
    req = requests.get(url = chapter_url)
    req.encoding = "utf-8"
    print(req.text)