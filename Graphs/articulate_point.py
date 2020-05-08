from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    """
    A recursive function that finds articulation points using dfs travel

    u --- > the vertex to be visited next
    visited[] ---> keeps track of visited vertices
    disc[] ---> stores the discovery time of visited vertex
    parent[] ---> Stores parent vertices in the dfs tree
    ap[] ---> store articulate points
    """

    def articulate_point_util(self,u,visited,ap,parent,low,disc):
        # count of children in current node
        children = 0

        # mark the current node as visited and print it
        visited[u] = True

        # initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        # recur for all the vertices adjcent to this vertex
        for v in self.graph[u]:
            # if v is not visited yet than make it the child of u
            # in the DFS tree and recure for it

            if visited[v] == False:
                parent[v] = u
                children += 1
                self.articulate_point_util(v,visited,ap,parent,low,disc)

                # check if the subtree rooted with v has a connection to one of the ancestors of u

                low[u] = min(low[u],low[v])

                # u is the articulate point in the following cases
                # (1) u is root of DFS tree and has two or more childrens
                if parent[u] == -1 and children > 1:
                    ap[u] = True
                # (2) if u is not root and low value of one of its child is more than discovery value of u

                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True
            elif v != parent[u]:
                low[u] = min(low[u],disc[v])

    def articulate_point(self):
        # mark all the vertices as not visited and initialize the parent and visited and ap arrays

        visited = [False] * (self.vertices)
        disc = [float("inf")] * self.vertices
        low = [float("inf")] * self.vertices
        parent = [-1] * self.vertices
        ap = [False] * self.vertices 
        # call the recursive helper function to find the articulation points in the DFS tree rooted with vertex 'i'

        for i in range(self.vertices):
            if visited[i] == False:
                self.articulate_point_util(i,visited,ap,parent,low,disc)

        for index,value in enumerate(ap):
            if value == True:
                print(index)
    

"""
from  collections import defaultdict
class Graph:
	def __init__(self,vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)
		self.Time = 0

	def add_edge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

		def articulate_points_util(self,u,visited,ap,parent,low,disc):
			children = 0
			visited[u] = True
			disc[u] = self.Time
			low[u] = self.Time
			self.Time += 1

			for v in self.graph[u]:
				if visited[v] == False:
					parent[v] = u
					children += 1
					self.articulate_point_util(v,visited,ap,parent,low,disc)
					low[u] = min(low[u],low[v])
					if parent[u] == -1 and low[v] >= disc[u]:
						ap[u] = True
				elif v != parent[u]:
					low[u] = min(low[u],disc[v])
		def articulate_point(self):
			visited = [False] * self.vertices
			disc = [float("inf")] * self.vertices
			low = [float("inf")] * self.vertices
			parent = [-1] * self.vertices
			ap = [False] * self.vertices

			for i in range(self.vertices):
				if visited[i] == False:
					self.articulate_point_util(i,visited,ap,parent,low,disc)

			for index,value in enumerate(ap):
				if value == True:
					print(index)
"""

        