import builtins
import collections
default = {
'spam': 'default spam value',
'eggs': 'default eggs value',
}
mappings = collections.ChainMap(globals(), locals(), vars(builtins))
print(mappings['default'])
