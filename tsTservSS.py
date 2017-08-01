#!/usr/bin/env python

from socketserver import (TCPServer as TCP,
	StreamRequestHandler as SRH)

from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
	def handle(self):
		print('...Connected from:', self.client_address,
			self.wfile.write('[%s] %s'%(ctime(), self.rfile.readline())))
tcpServ = TCP(ADDR, MyRequestHandler)
print('waittin for connection ...')
tcpServ.serve_forever()		