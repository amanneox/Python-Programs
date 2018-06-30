import numpy as np

def test(expenditure, d):
    i=0
    c=0
    l=list()
    for x in expenditure:
        i=i+1
        l.append(x)
        if i==d:
            l=list()
            m = np.median(l)
            print(m)
            if m >= 2*x:
                c=c+1
    
    print(c)
test([2,3,4,2,3,6,8,4,5],5)
