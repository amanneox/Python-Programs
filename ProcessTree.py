import json
import functools
import collections
def tree():
    return collections.defaultdict(tree)
taxonomy = tree()
reptilia = taxonomy['Chordata']['Vertebrata']['Reptilia']
reptilia['Squamata']['Serpentes']['Pythonidae'] = ['Liasis', 'Morelia', 'Python']
print(json.dumps(taxonomy, indent=4))

path='Chordata.Vertebrata.Reptilia.Squamata.Serpentes'
path=path.split('.')

family = functools.reduce(lambda a, b: a[b], path, taxonomy)
family.items()
dict_items([('Pythonidae', ['Liasis', 'Morelia', 'Python'])])
