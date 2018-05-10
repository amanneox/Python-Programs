class DistinctError(Exception):
    pass
class distinctdict(dict):
    def __setitem__(self,key,value):
        try:
            value_index=list(self.values()).index(value)
            existing_key=list(self.keys())[value_index]
            if existing_key !=key:
                raise DistinctError("Error:",self[existing_key])
        except ValueError:
            pass
        super(distinctdict,self).__setitem__(key,value)

my=distinctdict()
my['key']='value'
my['other_key'] = 'value'
my['other_key'] = 'value2'
print(my)
