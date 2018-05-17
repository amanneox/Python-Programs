import json
import functools
import collections
def tree():
    return collections.defaultdict(tree)
taxonomy = tree()
reptilia = taxonomy['Chordata']['Vertebrata']['Reptilia']
reptilia['Squamata']['Serpentes']['Pythonidae'] = ['Liasis', 'Morelia', 'Python']
print(json.dumps(taxonomy, indent=4))
