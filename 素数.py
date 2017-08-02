'''打印100以内的素数'''
def func(n):
	if n < 1:
		return
	for i in range(2, n):
		sqr = int(sqrt(n))
		for j in range(2, sqr+1):
			if i%j == 0:
				break
		print(i, end=' ')
