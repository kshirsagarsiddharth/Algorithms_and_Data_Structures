from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices
        self.visited_list = defaultdict()
        self.output_stack = []
    
    def add_edge(self,From,To):
        self.graph[From].append(To)
        self.visited_list[From] = False
        self.visited_list[To] = False
    
    def topological_sort_util(self,vertex):
        if not self.visited_list[vertex]:
            self.visited_list[vertex] = True
            for neighbour in self.graph[vertex]:
                self.topological_sort_util(neighbour)
            self.output_stack.insert(0,vertex)
    
    def topology_sort(self):
        for vertex in self.visited_list:
            self.topological_sort_util(vertex)                

"""
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited_list = defaultdict()
        self.output_stack = []
    
    def add_edge(self,From,To):
        self.graph[From].append(To)
        self.visited_list[From] = False
        self.visited_list[To] = False
    
    def topological_sort_util(self,vertex):
        if not self.visited_list[vertex]:
            self.visited_list[vertex] = True
        for neighbors in self.graph[vertex]:
            self.topological_sort_util(self,neighbors)
        return self.output_stack.insert(0,vertex)
    
    def topological_sort(self):
        for vertex in self.visited_list:
            self.topological_sort_util(vertex)
            

"""
class Graph_two: 
    def __init__(self,vertices): 
		self.graph = defaultdict(list) #dictionary containing adjacency List 
		self.V = vertices #No. of vertices 

	# function to add an edge to graph 
    def addEdge(self,u,v): 
		self.graph[u].append(v) 

    def topological_sort_util(self,v,visited,stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_util(i,visited,stack)

        stack.insert(0,v)
    
    def toploogical_sort(self):
        visited = [False] * self.vertices
        stack = []

        for i in range(self.vertices):
            if visited[i] == False:
                self.topological_sort_util(i,visited,stack)
        
        return stack
    
