import math

def isPrime(x):
	if x < 2:
		return False
	sqr = int(math.sqrt(x))
	i = 2
	while i <= sqr:
		if x % i == 0:
			return False
		else:
			i += 1
	return True

flag = True
result = []
for i in range(100):
	if isPrime(i):
		result.append(i)

print(' '.join(str(i) for i in result))

#埃氏素数筛选法
table = [True]*1000
#为单独的0和1设置为false
table[0] = table[1] = False
for i in range(2, 101):
	if table[i]:
		for k in range(2*i, 101, i):
			table[k] = False

for i in range(101):
	if table[i]:
		print(i, end = ' ')