"""公约数的个数"""
def func(a, b):
	cnt = 0
	i = 1
	while i <= min(a, b):
		if a%i == 0 and b%i == 0:
			cnt += 1
		i += 1
	return cnt
print(func(24, 36))