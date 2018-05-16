import collections

ol=collections.OrderedDict()

ol['a']=10
ol['b']=20
ol['c']=30

print([value for value in ol.items()])
