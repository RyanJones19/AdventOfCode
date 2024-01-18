import sys
from collections import defaultdict
import networkx as nx

data = open(sys.argv[1]).read().strip().split('\n')
graph = [[col for col in row] for row in data]

edgeSet = defaultdict(set)
for line in data:
  vertex, edges = line.split(':')
  for edge in edges.split():
    edgeSet[vertex].add(edge)
    edgeSet[edge].add(vertex)

graph = nx.DiGraph()
for key, vals in edgeSet.items():
  for val in vals:
    graph.add_edge(key, val, capacity=1.0)

for vertex1 in [list(edgeSet.keys())[0]]:
  for vertex2 in edgeSet.keys():
    if vertex1!=vertex2:
      cut_value, (set1, set2) = nx.minimum_cut(graph, vertex1, vertex2)
      if cut_value == 3:
        print(f"Part 1: {len(set1)*len(set2)}")
        break
