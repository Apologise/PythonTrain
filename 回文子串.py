'''
给你一个字符串a和一个正整数n,判断a中是否存在长度为n的回文子串。如果存在，则输出YES，否则输出NO。
回文串的定义：记串str逆序之后的字符串是str1，若str=str1,则称str是回文串，如"abcba".
'''

def func(str, n):
	liststr = list(str)
	length = len(str)
	if not str:
		return False
	if  length == 1:
		return True
	for i in range(0, length -n+1):
		 temp = ''.join(liststr[i:n+i])
		 temp_reverse = temp[::-1]
		 if temp_reverse == temp:
		 	return True

strs = 'acdca'
if func(strs, 6):
	print('YES')
else:
	print('NO')
