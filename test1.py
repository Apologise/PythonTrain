from bs4 import BeautifulSoup
import re
import requests
r = requests.get("http://www.123huodong.com/ykvip/2017/0606/146478.html")
r.encoding = "utf-8"
soup = BeautifulSoup(r.text,'lxml')
print(soup.find_all('DIV',{'p':re.compile('账号')}))
