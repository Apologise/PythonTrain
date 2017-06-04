# -*- coding: utf-8 -*-
"""
Created on Wed May 31 10:06:25 2017

@author: Administrator
"""

import requests
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
       
        print(r.raise_for_status())
        r.encoding = 'utf-8'
        return r.text,r.content
    except:
        return ""
url = "http://www.baidu.com"
html = getHTMLText(url)
t = html[0]
c = html[1]
print(len(t))
print(len(c))