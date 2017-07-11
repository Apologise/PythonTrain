daxie = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖','','拾','佰','仟','万','拾','佰','仟']
def func(num):
	result = ''
	if num < 0:
		result += '负'
		num = abs(num)

	cnt = 0
	while num != 0:
		if cnt == 1:
			result += '拾'
		if cnt == 2:
			result += '佰'
		if cnt == 3:
			result += '仟'
		if cnt == 4:
			result += '万'
		i = int(num % 10)
		num =  int(num/10)
		result = result + daxie[i]
		cnt += 1
	return result[::-1]
print(func(111))