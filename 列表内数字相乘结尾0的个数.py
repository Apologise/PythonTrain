
"""
思路：边乘边除
"""
def total_zero(lst):
	total = 1
	sum = 0
	for i in lst:
		total *= i
		while total % 10 == 0:
			total /= 10
			sum += 1
	return sum

lst = [2, 8, 3, 50]
print(total_zero(lst))

"""
	统计每个数中因数2和五的个数
"""

def total_zero1(lst):
	num2 = 0
	num5 = 0
	for i in lst:
		while i % 5 == 0:
			num5 += 1
			i /= 5
		while i % 2 == 0:
			num2 += 1
			i /= 2
	return min(num2, num5)

print(total_zero1(lst))