'''
给你一个时间t（t是一个字典，共有六个字符串key(year,month,day,hour,minute,second),值为每个值为数字组成的字符串，
如t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}
请将其按照以下格式输出， 格式:XXXX-XX-XX XX:XX:XX。如上例应该输出： 2013-09-30 16:45:02。
'''

def func(dic):
	year,month, day = dic['year'], dic['month'], dic['day']
	hour, minute, second = dic['hour'], dic['minute'], dic['second']
	print('{0:0>4}-{1:0>2}-{2:0>2} {3:0>2}:{4:0>2}:{5:0>2}'.format(year, month, day, hour, minute, second))

t = {'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}

func(t)