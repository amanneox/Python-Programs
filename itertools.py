import functools
import itertools
import operator
months=[x for x in range(10,20) if x%3 or x%4]
print(months)
print(list(itertools.accumulate(months,operator.add)))


a=range(5)
b=range(10)
print(list(itertools.chain(a,b)))

print(list(itertools.combinations(range(3),2)))

print(list(itertools.dropwhile(lambda x:x<=3,[1,2,3,4,5])))

print(list(itertools.takewhile(lambda x:x<5,[1,2,3,4,5])))
