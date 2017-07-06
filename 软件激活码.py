from math import sqrt

def func(n):
	result = 0
	count = 0
	for k in range(1,n+1):
		for i in range(k):
			result += pow(2, i)
			count +=1
			if count == n:
				return result
	

def is_func(n):
	return (n&(n-1))==0

N = 101
i = 1
result = 0
while i:
	result = func(i)
	if i > 100 and is_func(result):
		print(i)
		break
	i += 1

