from collections import defaultdict

class Graph:

    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_util(self,v,visited,stack):
        visited[v] = True
        stack.append(v)

        for i in self.graph[v]:
            if visited[i] == False:
                stack = self.dfs_util(i,visited,stack)
        
        return stack

    def connected_components(self):
        visited = [False] * self.vertices

        #stack = []
        connected_comps = []

        for i in self.graph:
            if visited[i] == False:
                stack = []
                connected_comps.append(self.dfs_util(i,visited,stack))
        return connected_comps

g = Graph(5)
g.add_edge(1,0)
g.add_edge(2,3)
g.add_edge(3,4)
print(g.connected_components())

        