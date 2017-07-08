def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a%b)

def func(a,b):
	temp = a*b
	return int(temp/gcd(a,b))

print(func(15,6))