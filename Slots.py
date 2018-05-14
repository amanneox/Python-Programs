class Frozen(object):
    __slots__=['ice','cream']
x=Frozen()
print('ice' in dir(Frozen))
print('milk' in dir(Frozen))
