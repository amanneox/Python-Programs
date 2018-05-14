import collections
deque=collections.deque()
deque.append(5)
deque.append(3)
print(deque)
deque.popleft()
print(deque)
deque.append([i for i in range(10)])
print(deque.pop())
