


"""
DFS ALGORITHM

1 - Start by adding and one of the graph's vertices on the top of a stack,
2 - Take the top item of the stack and add it to the visited list
3- Create a list of that vetrex's adjcent nodes. Add the the nodes which are not in the visited list to the top of the stack
4 - keep repeting steps two and three until the stack is empty

"""
visited = set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neigbhour in graph[node]:
            dfs(visited,graph,neigbhour)

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs_i(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()       
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
"""
def dfs_iterative(graph,start):
    visited,stack = set(),[start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
"""
def dfs_r(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
"""
def dfs_recursive(graph,start,visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs_recursive(graph,next,visited)
    return visited
"""
def dfs_paths_iterative(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
def dfs_paths_i(grapg,start,goal):
    stack = [(start,[start])]
    while stack:
        (vertex,path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next,path + [next]))

def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])



graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

for i in dfs_paths(graph,'C','F'):
    print(i)

