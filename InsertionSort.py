import random
l=[random.randint(1,100) for x in range(10)]
print(l)
for x in range(1,len(l)):
    key=l[x]
    i=x-1
    while i>=0 and l[i]>key:
        l[i+1]=l[i]
        i=i-1
    l[i+1]=key

print(l)
