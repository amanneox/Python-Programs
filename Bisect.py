import bisect
from random import *

sorted_list=[x for x in range(10)]
shuffle(sorted_list)

print(sorted_list)

def contains(sorted_list, value):
    i = bisect.bisect_left(sorted_list, value)
    return i < len(sorted_list) and sorted_list[i] == value

print(contains(sorted_list,9))
