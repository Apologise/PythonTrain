strings = ['asdfgyanghao', 'asdfweior', 'yanghao', 'asdf','asdyanghao']
index  = 0
for string in strings:
	if 'yanghao' in string:
		strings[index] = '[test]'
	index += 1
print(strings)
print(strings[1])