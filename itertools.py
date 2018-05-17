import functools
import itertools
import operator
months=[x for x in range(10,20) if x%3 or x%4]
print(months)
print(list(itertools.accumulate(months,operator.add)))


a=range(5)
b=range(10)
print(list(itertools.chain(a,b)))
