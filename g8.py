#Given an array of integers where every integer occurs three times #except for
#one integer, which only occurs once, find and return #the non-duplicated integer.

#For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, #19, 13, 13], return 19.
from collections import *

array = [6,1,3,3,3,6,6]
array1 = [13, 19, 13, 13]
counter = 1
d = Counter(array1)

def fun(d):
    for keys,values in d.items():
        if values != 3:
            return keys

x = fun(d)
print(x)
