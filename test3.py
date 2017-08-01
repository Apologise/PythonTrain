import urllib.request
import urllib.parse

url = 'http://www.pythontip.com/user/login'
postdata = urllib.parse.urlencode({
	'name':'yanghao19950112',
	'pwd':'13409705827.'
	}).encode('utf-8')
print('读写开始')
req = urllib.request.Request(url,postdata)
req.add_header('User-Agent',"Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0")
print('读写过程中')
data = urllib.request.urlopen(req).read()
print('读写中')
fhandle = open('test3.html', 'wb')
fhandle.write(data)
print('读写完成')
fhandle.close()



def use_proxy(proxy_addr, url):
	import urllib.request
	proxy = urllib.request.ProxyHandler({'http':proxy_addr})
	opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
	urllib.request.install_opener(opener)
	data = urllib.request.urlopen(url).read().decode('utf-8')
	return data
'''
proxy_addr = '123.116.91.156:8118'
data = use_proxy(proxy_addr, 'http://www.baidu.com')
print(len(data))
'''