from collections import defaultdict

graph = defaultdict(list)
def add_edge(From,To):
    graph[From].append(To)
    
    
        
def find_shortest_path(source):
    #parent = {source:None}
    parent = dict()
    distance = dict()
    visited = set()
    queue = []
    parent[source] = None
    distance[source] = 0
    queue.append(source)
    visited.add(source)
    while len(queue) > 0:
        current = queue.pop(0)
        for dest in graph[current]:
            if dest not in visited:
                visited.add(dest)
                parent[dest] = current
                distance[dest] = distance[current] + 1
                queue.append(dest)
    return parent,distance


add_edge(2,1)
add_edge(1,2)
add_edge(1,0)
add_edge(0,1)
add_edge(0,3)
add_edge(3,0)
add_edge(3,7)
add_edge(7,3)
add_edge(3,4)
add_edge(4,3)
add_edge(7,4)
add_edge(4,7)
add_edge(7,6)
add_edge(6,7)
add_edge(4,6)
add_edge(6,4)
add_edge(6,5)
add_edge(5,6)
add_edge(4,5)
add_edge(5,4)

print(find_shortest_path(7))
