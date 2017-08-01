#! /usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21563
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
	print('Waitting for connection...')
	tcpCliSock, addr = tcpSerSock.accept()
	print('...Connected from :', addr)

	while True:
		data = bytes(tcpCliSock.recv(BUFSIZ))
		if not data:
			break
		#tcpCliSock.send('[%s] %s' %
		 #(bytes(ctime(), encoding='utf-8'), bytes(data, encoding ='utf-8')))
		tcpCliSock.send('[%s] %s'%(
			bytes(ctime()), bytes(data)))
	tcpCliSock.close()
tcpSerSock.close()