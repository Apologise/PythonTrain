def func(num):
	cnt = 0
	while num!=0:
		temp = num % 2
		num = int(num/2)
		if temp == 1:
			cnt += 1
	return cnt
print(func(15))
