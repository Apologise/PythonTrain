def func(lst):
	result = 1
	for i in lst:
		result *= i
		while result%10 == 0:
			result /= 10
	if result%2 == 0:
		result = 0
	else:
		result = 1
	return result

L = [2,3,1]
print(func(L))