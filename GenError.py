def my_gen():
 try:
    yield 'No errors'
 except ValueError:
    yield 'Something went wrong'
 finally:
     yield 'Ok, Move on'


x=my_gen()
y=next(x)
print(y)
e=x.throw(ValueError('error')) # throw an error
print(e)
c=x.close() #Raise a generator exit exception
print(c)
