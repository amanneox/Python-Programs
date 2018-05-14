import collections
counter=collections.Counter('eggs')
for k in 'eggs':
     print('Count for %s: %d' % (k, counter[k]))

counter2=collections.Counter()
for i in range(0,100):
    counter2[i]+=i

for key, count in counter2.most_common(5):
     print('%s: %d' % (key, count))
