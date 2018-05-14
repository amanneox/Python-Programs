class Myclass(object):
    def __new__(cls):
        print("__new__ called")
        return object.__new__(cls)
    def __init__(self):
        print("__init__ called")
        self.a=1

x=Myclass()
print(x.a)
