import requests
from bs4 import BeautifulSoup
import json

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

def parse(pageString):
    try:
        bsObj = BeautifulSoup(pageString, "html.parser")
        aTag = bsObj.find("div", {"class":"k_Q0X"})
        script = bsObj.find("script", {"type":"application/ld+json"})
        jsonObj = json.loads(script.text)
        print(jsonObj['uploadDate'])

    except:
        print("에러발생")
    return {}

def get_imgs(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    metaTag = bsObj.find("meta", {"property":"og:image"})
    print(bsObj.find_all("meta"))
    print(metaTag["content"])

    return metaTag["content"]

if __name__ == "__main__":
    url = "https://www.instagram.com/p/B3UArptgW3v/"
    pageString = crawl(url)
    get_imgs(pageString)
    print(get_imgs)