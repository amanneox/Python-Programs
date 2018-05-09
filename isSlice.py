import itertools
def start_at_five():
    value=input().strip()
    while value !='':
        for i in itertools.islice(value.split(),4,None):
            yield i
        value=input().strip()

iter=start_at_five()
