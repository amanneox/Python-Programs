import collections


def mode(arr):
    input()
    count = [0] * 6
    for t in map(int, input().strip().split()):
        count[t] += 1
    print(count.index(max(count)))


mode(arr=[1, 4, 4, 4, 5, 3])
