"""
While T is not yet a spanning tree
Find an edge that is safe to add to the tree
Add the new edge to T
"""
# PRIMS ALGORITHM
from collections import defaultdict
import heapq

def create_spanning_tree(graph,source):
    mst = defaultdict(set)
    visited = set([source])
    edges = [
        (cost,source,to) for to,cost in graph[source].items()
    ]
    heapq.heapify(edges)
    while edges:
        cost,frm,to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges,(cost,to,to_next))
    return mst

example_graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1},
    'G': {'F': 1},
}