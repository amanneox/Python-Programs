import itertools
seq=list(range(10))
a,b=itertools.tee(seq)
print([next(a) for i in range(10)])
print([next(b) for i in range(10)])
