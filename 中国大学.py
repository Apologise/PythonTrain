from bs4 import BeautifulSoup
import requests
import re
allUniv = []
def fillUnivList(soup):
    data = soup.find_all('tr')
    for tr in data:

        itd = tr.find_all('td')
        if len(itd) == 0:
            continue
        singleUniv = []
        for td in itd:
            singleUniv.append(td.string)
        allUniv.append(singleUniv)

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ''

def printUnivList(num):
    print("{:^4}{:^4}{:^4}{:^4}{:^4}".format('排名','学校名称','省市','总分','培养规模'))
    for i in range(num):
        u = allUniv[i]
        print("{:^4}{:^10}{:^5}{:^8}{:^10}".format(u[0],u[1],u[2],u[3],u[6]))

def main(num):
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, 'lxml')
    fillUnivList(soup)
    printUnivList(num)
main(10)