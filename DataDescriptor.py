class UpperString(object):
    def __init__(self):
        self._value=''
    def __set__(self,instance,value):
        self._value=value.upper()
    def __get__(self,instance,klass):
        return self._value

class MyClass(object):
    attribute = UpperString()

instance_of = MyClass()
print(instance_of.attribute)
instance_of.attribute='my value'
print(instance_of.attribute)
