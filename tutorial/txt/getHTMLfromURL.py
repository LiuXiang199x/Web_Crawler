import requests

if __name__ == "__main__":
    target = "https://fanyi.baidu.com/"
    req = requests.get(url = target)
    req.encoding = "utf-8"
    print(req.text)