from itertools import groupby
def compress(data):
      return ((len(list(group)), name)
      for name, group in groupby(data))

def decompress(data):
      return (car * size for size, car in data)

y=list(compress('get uuuuuuuuuuuuuuuuuup'))
print(y)
compressed = compress('get uuuuuuuuuuuuuuuuuup')
print(''.join(decompress(compressed)))
