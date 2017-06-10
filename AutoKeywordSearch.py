import requests
from bs4 import BeautifulSoup
import re
import json

def getKeywordResult(keyword):
    url = "http://www.baidu.com/s?wd=" + keyword
    try:
       r=requests.get(url, timeout = 30)
       r.raise_for_status()
       r.encoding = 'utf-8'
 #      print(r.text)
       return r.text
    except:
        return ""

def parseLinks(html):
    soup = BeautifulSoup(html,'lxml')
    links = []
    data = soup.find_all('h3',{'class':'t'})

    for value in data:
        print(value)
        d = value.find_all('em')
        print(d.string)
        links.append(d.string)
    return links

def main():
    html = getKeywordResult('Python语言程序设计基础(第二版)')
    ls = parseLinks(html)
    count  = 1
    for i in ls:
        print("[{:^3}]".format(count, i))
        count += 1
main()