from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats = array('d')
fp = open('floats.bin', 'rb')
floats.fromfile(fp, 10**7)
print(floats[-1])