import heapq
heap = [9, 3, 5, 7, 2, 4, 3]
heapq.heapify(heap)
print(heap[0]) # minimum number at top
while heap:
    print(heapq.heappop(heap), heap)
