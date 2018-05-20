import functools

#without functools.warp()

def eggs(function):
    def _eggs(*args,**kwargs):
        return function(*args,**kwargs)
    return _eggs

@eggs
def spam(a,b,c):
    '''The spam function Returns a * b + c'''
    return a * b + c

help(spam)            
