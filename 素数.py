'''打印100以内的素数'''
def func(n):
	if n < 1:
		return
	for i in range(2, n):
		sqr = int(sqrt(n))