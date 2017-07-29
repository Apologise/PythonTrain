class Test():
	def __init__(self):
		print('我被初始化了')

	def __call__(self):
		print('我被调用了')

test = Test()
test()