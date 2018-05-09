import threading
import time
def coroutine_1():
    for i in range(3):
        print('c1')
        yield i
def coroutine_2():
    for i in range(3):
        print('c2')
        yield i

t1 = threading.Thread(target=coroutine_1, args=[])
t2 = threading.Thread(target=coroutine_2, args=[])
t1.run()
t2.run()
