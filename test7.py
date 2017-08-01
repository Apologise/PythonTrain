import re

pattern = 'python|php'
string = 'abcdfphp345pythony_py'
#python, php
result1 = re.search(pattern, string)
print(result1)