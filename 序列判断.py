

def func(L):
	up_str = sorted(L)
	down_str = sorted(L, reverse=True)
	if L == up_str：
		print('UP')
	elif L == down_str:
		print('DOWN')
	else:
		print('WRONG')

func(L)
