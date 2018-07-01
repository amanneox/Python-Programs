import math
import random

# Complete the insertionSort function below.
'''
Code fails due to time complexity apply divide and conquer test #1
'''
def insertionSort(arr):
    print(arr)
    k=list()
    c=0
    for x in range(1,len(arr)):
        key=arr[x]
        i=x-1
        while i>=0 and arr[i]>key:
            c=c+1
            arr[i+1]=arr[i]
            i=i-1
        arr[i+1]=key
        k.append(c)
        c=0
    print(arr)
    print(k)

insertionSort(arr=[4,3,2,1])
#insertionSort([random.randint(1,10) for x in range(5)])
