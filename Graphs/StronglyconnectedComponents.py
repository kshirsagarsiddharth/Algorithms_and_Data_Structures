from collections import defaultdict

class Graph:

    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

        def add_edge(self,u,v):
            self.graph[u].append(v)

        def dfs_util(self,v,visited):
            # mark the current node as visited and print it
            visited[v] = True
            print(v)
            for i in graph[v]:
                if visited[i] == False:
                    self.dfs_util(i,visited)

        def fill_order(self,v,visited,stack):
            visited[v] = True
            for i in self.graph[v]:
                if visited[i] == False:
                    self.fill_order(i,visited,stack)
            stack = stack.append(v)
        
        def get_transpose(self):
            g = Graph(self.vertices)

            # recur for all the vertices adjcent to this vertex
            for i in self.graph:
                for j in self.graph[i]:
                    g.add_edge(j,i)
            return g
        # this is the main function of this graph which finds and prints the strongly connected components
        def print_ssc(self):
            stack = []
            # mark all the vertices as not visited (fro first dfs)
            visited = [False] * self.vertices
            # fill the vertices in the stack according to their finishing times

            for i in range(self.vertices):
                if visited[i] == False:
                    self.fill_order(i,visited,stack)
            
            # create a eversed grapg
            gr = self.get_transpose()

            # mark all the vertices as not visited for DFS second time
            visited = [False] * (self.vertices)

            # now process all the vertices in the order defined by the stack
            while stack:
                i = stack.pop()
                if visited[i] == False:
                    gr.dfs_util(i,visited)
                print("")
            

"""
from collections import defaultdict
class Graph:

	def __init__(self,vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)

	def add_edge(self,u,v):
		self.graph[u].append(v)
	
	def dfs_util(self,v,visited):
		visited[v] = True
		print(v)
		for i in graph[v]:
			if visited[i] == False:
				self.dfs_util(i,visited)
	
	def fill_order(self,v,visited,stack):
		visited[v] = True
		for i in self.graph[v]:
			if visited[i] == False:
				self.fill_order(i,visited,stack)
		stack = stack.append(v)
	
	def get_transpose(self):
		g = Graph(self.vertices)

		for i in self.graph:
			for j in self.graph[i]:
				g.add_edge(j,i)
		return g

	def print_ssc(self):
		stack = []
		visited = [False] * self.vertices

		for i in range(self.vertices):
			if visited[i] == False:
				self.fill_order(i,visited,stack)
		gr = self.get_transpose()

		visited = [False] * self.vertices

		while stack:
			i = stack.pop()
			if visited[i] == False:
				gr.dfs_util(i,visited)
			print("")
"""
