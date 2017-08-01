import re
pattern1 = 'py.*n'
pattern2 = 'cd{2}'
pattern3 = 'cd{3}'
pattern4 = 'cd{2,}'
string = 'avcdddfphp345pythony_py'
#python
#cddd
#cddd
#cddd
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
result4 = re.search(pattern4, string)
print(result1)
print(result2)
print(result3)
print(result4)