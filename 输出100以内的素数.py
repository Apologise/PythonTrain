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