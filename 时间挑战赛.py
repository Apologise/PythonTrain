'''
给你两个时间st和et(00:00:00<=st <= et<=23:59:59), 请你给出这两个时间间隔的秒数。
如：st="00:00:00", et="00:00:10", 则输出10.
'''

def func(str1, str2):
	str1 = str1.split(':')
	str2 = str2.split(':')
	result1 = int(str1[0])*3600+int(str1[1])*60+int(str1[2])
	result2 = int(str2[0])*3600+int(str2[1])*60+int(str2[2])
	result = result1 - result2 if result1 > result2 else result2 - result1
	return result

print(func('01:00:00','00:00:10'))