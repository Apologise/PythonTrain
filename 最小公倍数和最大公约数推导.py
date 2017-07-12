"""
a*b/c = d
"""

def func(a, b):
	"""
	a为最大公约数，b为最小公倍数
	"""
	result = [0,0]
	tag = False
	temp = 0
	for i in range(a, b+1):
		if i%a == 0:
			if not tag:
				tag = True
				result[0] = i
				result[1] = a*b/i
			else:
				temp = i + a*b/i
				if temp < result[0] + result[1]:
					temp = result[0] + result[1]
					result[0] = i
					result[1] = int(a*b/i)

	return result

print(func(3, 60))
