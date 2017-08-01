import re
"""
pattern = 'yue'
pattern = re.compile(pattern)
string = 'http://yum,iqianyue.com'
result = re.search(pattern,string)
print(result)
"""
'''
pattern = '\spython\w'
string = 'abcdphp345 python_py'
result = re.search(pattern, string)
print(result)
'''

pattern1 = '\w\dpython[xyz]\w' 
pattern2 = '\w\dpython[^xyz]\w'
pattern3 = '\w\dpython[xyz]\W'
pattern4 = '.python...'
string = 'abcdfphp345pythony_py'
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
result4 = re.search(pattern4, string)
print(result1)
print(result2)
print(result3)
print(result4)