import collections

Point=collections.namedtuple('Point',['x','y','z'])

point_a=Point(1,2,3)

print(point_a)

x,y,z=point_a

print(x,y,z)
