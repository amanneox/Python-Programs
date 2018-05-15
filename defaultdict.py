import collections
import defaultdict
import pprint
nodes = [
('a', 'b'),
('a', 'c'),
('b', 'a'),
('b', 'd'),
('c', 'a'),
('d', 'a'),
('d', 'b'),
('d', 'c'),
]
graph = collections.defaultdict(list)
for from_, to in nodes:
    graph[from_].append(to)

pprint.pprint(graph)
