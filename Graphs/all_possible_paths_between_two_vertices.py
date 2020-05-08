"""
from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def count_paths(self,start,end):
        visited = [False] * [self.vertices]
        path_count = [0]
        self.count_paths_util(start,end,visited,path_count)
        return path_count
    
    def count_paths_util(self,start,end,visited,path_count):
        visited[start] = True
        if start == end:
            path_count[0] += 1
        else:
            for neighbor in self.graph[start]:
                self.count_path_util(neighbor,end,visited,path_count)
        visited[start] = False

"""


"""
algorithm
create a recursive function that takes index of node of a graph and the destination index.
keep a global or static variable to keep count of the vertices
if the current node is in the destination increase the count.
Else for all adjcent nodes i.e , nodes that are accessible from the current node, call the recursive function with the index of adjcent node and the destination.
print the count.
"""
from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def count_paths(self,s,d):
        # mark all the vertices as not visited
        visited = [False] * self.vertices

        # call the recursive helper function to print all the paths
        path_count = [0]
        self.count_paths_util(s,d,visited,path_count)
        return path_count[0]

    # a recursive function to print all paths from u to d. visited[] keeps track of vertices in current path. path[] stores actual vertices and path_index in current index in path[]

    def count_paths_util(self,u,d,visited,path_count):
        visited[u] = True

        # if the current vertex is same as the destination then increment count

        if u == d:
            path_count[0] += 1

        # if current vertex is not destination
        else:
            # recur for all the vertices adjcent to the current vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.count_paths_util(i,d,visited,path_count)
        
        visited[u] = False

g = Graph(4) 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(0, 3) 
g.add_edge(2, 0) 
g.add_edge(2, 1) 
g.add_edge(1, 3) 

s = 2
d = 3

print(g.count_paths(s,d))


