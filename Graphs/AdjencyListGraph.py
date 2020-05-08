"""
AdjList

Using dictonaries, it is easy to implement the adjacency list in python. In thos implementation we create two classes:
Graph, which holds the master list of vertices, and Vertex, which will represen each vertex in the graph.

Each Vertex uses a dictonary to keep track of the vertices to which it is connected, and weight of each edge. If we weren't concerned with the edge weights, we could use a set in place of the dictonary. This dictonary is called the neighbors.
"""

class Vertex:
    def __init__(self,key):
        self.key = key
        self.neighbors = {}

    def add_neighbours(self,neighbor,weight = 0):
        self.neighbors[neighbor] = weight
    
    def __str__(self):
        return '{} neighbos: {}'.format(self.key,[x.key for x in self.neighbors])
    
    def get_connections(self):
        return self.neighbors.keys()

    def get_weight(self,neighbour):
        return self.neighbors[neighbour]
"""

class Vertex:
    def __init__(self,key):
        self.key = key
        self.neighbors = {}

    def add_neighbors(self,neighbour,weight = 0):
        self.neighbors[neighbour] = weight
    
    def __str__(self):
        return '{} neighbors: {}'.format(self.key,[x.key for x in self.neighbors])

    def get_connections(self):
        return self.neighbors.keys()

    def get_weight(self,neighbor):
        return self.neighbours[neighbour]
"""
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,vertex):
        self.vertices[vertex.key] = vertex

    def get_vertex(self,key):
        try:
            return self.vertices[key]
        except ValueError:
            return None 
    
    def add_edge(self,from_key,to_key,weight = 0):
        if from_key not in self.vertices:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.vertices:
            self.add_vertex(Vertex(to_key))
        self.vertices[from_key].add_neighbours(self.vertices[to_key],weight)

    def get_vertices(self):
        return self.vertices.keys()
    
    def __contains__(self,key):
        return key in self.vertices 
    
    def __iter__(self):
        return iter(self.verticies.values())
    

#ver2 = Vertex(1,{2:4})