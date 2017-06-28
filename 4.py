a = {1:1, 2:2, 3:3}
count = 0
for i in a.keys():
	if count != len(a.keys()) - 1:
		print(i, end=',')
		count += 1
	else:
		print(i)