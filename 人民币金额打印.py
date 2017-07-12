daxie = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖','','拾','佰','仟','万','拾','佰','仟']
def func(num):
	result = ''
	if num < 0:
		result += '负'
		num = abs(num)

	cnt = 0
	tagzero = False
	left = True
	while num != 0:
		i = int(num % 10)
		if left and i == 0:
			cnt += 1
			num = int(num/10)
			tagzero = True
			continue

		if i == 0:
			tagzero = True
			num = int(num/10)
			cnt += 1
			continue

		if i != 0 and tagzero and not left:
			result += '零'
			left = False
			tagzero =  False

		tagzero = False
		if cnt == 1 and not tagzero:
			result += '拾'
		if cnt == 2 and not tagzero:
			result += '佰'
		if cnt == 3 and not tagzero:
			result += '仟'
			print(tagzero, i)
		if cnt == 4 and not tagzero:
			result += '万'

		num =  int(num/10)
		result = result + daxie[i]
		cnt += 1
		left =  False
	return result[::-1]
print(func(300110))