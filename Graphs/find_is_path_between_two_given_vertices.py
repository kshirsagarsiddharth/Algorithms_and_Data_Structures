from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def is_reachable(self,s,d):
        # mark all the vertices as not visited
        visited = [False] * (self.vertices)

        # create a queue for BFS

        queue = []

        # mark the source node as vsisted and enque it
        queue.append(s)
        visited[s] = True

        while queue:

            # deaue a vertex from the queue
            n = queue.pop(0)

            # if the adjcent node is the destination node than return true
            if n == d:
                return True
            
            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        # if the bfs is compleated without visited d
        return False

g = Graph(4) 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 

u = 1
v = 3

"""
from collections import defaultdict
class Graph:
	def __init__(self,vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)
	
	def add_edge(self,u,v):
		self.graph[u].append(v)
	
	def is_connected(self,start,end):
		queue = []
		visited = [False] * self.vertices
		queue.append(start)
		visited[start] = True

		while queue:
			n = queue.pop(0)

			if n == end:
				return True
			
			for neighbour in graph[n]:
				if visited[neighbour] == False:
					queue.append(neighbour)
					visited[neighbour] = True
		
		return False
"""
