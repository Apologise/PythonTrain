import re
pattern1 = '^abd'
pattern2 = '^abc'
pattern3 = 'py$'
pattern4 = 'ay$'
string = 'abcdfphp345pythony_py'
#None
#abc
#py
#None
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
result4 = re.search(pattern4, string)
print(result1)
print(result2)
print(result3)
print(result4)