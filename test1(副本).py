import urllib.request
url = 'http://www.baidu.com'
headers = ("Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0")
req = urllib.request.Request(url)
req.add_header("Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0")
data = urllib.request.urlopen(req).read()