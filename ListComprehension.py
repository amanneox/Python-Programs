import random

print([(x, y) for x in range(3) for y in range(3, 5)])

print({y: x**2 for x in range(10) for y in range(3,5)})

print({x+y for x in range(3) for y in range(3)})
