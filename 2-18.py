import bisect
import sys
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
	i = bisect.bisect(breakpoints, score)
	print('test:', i)
	return i
	
print([grade(score) for score in [30, 99, 77, 70, 89, 90 ,100]])
