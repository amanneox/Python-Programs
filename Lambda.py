Y = lambda f: lambda *args: f(Y(f))(*args)
def factorial(combinator):
    def _factorial(n):
        if n:
            return n * combinator(n - 1)
        else:
            return 1
    return _factorial
x=Y(factorial)(5)

y=Y(lambda c: lambda n: n * c(n - 1) if n else 1)(5)

print(x,y)
