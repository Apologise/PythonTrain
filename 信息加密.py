def func(strs, offset):
	strs = list(strs)
	for i in range(len(strs)):
		strs[i] = chr(((ord(strs[i])-97)+offset)%26+97)
	return ''.join(i for i in strs)
print(func('cagy', 3))
