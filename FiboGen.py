def fibo():
    a,b=0,1
    while True:
        yield b
        a,b=b,a+b

fib=fibo()
print([next(fib) for i in range(10)])
