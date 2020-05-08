from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs_util(self,v,visited):
        # mark the current node as visited
        visited[v] = True

        # recur for all the vertices adjcent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.def_util(i,visited)
    
    """
    Method to check ia all non-zero degree vertices are connected or not.
    It dose dfs starting from node  with noe-zero degree.
    """

    def is_connected(self):
        # mark all the vertices as non visited
        visited = [False] * (self.vertices)

        # find vetex with non-zero degree
        for i in range(self.vertices):
            if len(self.graph[i]) > 1:
                break
        # if there are no edges in the graph return true
        if i == self.vertices - 1:
            return True

        # start DFS traversal from a vertex with non zero degrees
        self.dfs_util(i,visited)

        # check if all non-zero degree vertices are visited
        for i in range(self.vertices):
            if visited[i] == False and len(self.graph[i] > 0):
                return False
        
        return True

    
	"""
	This function returns one of the following values

	0 -- if the graph is not eulerian
	1 -- if the graph has an euler path
	2 -- if the graph has eulerian circuit
	"""

	def is_eulerian(self):
		if self.is_connected() is False:
			return 0
		else:
			# count the vertices with odd edges
			odd = 0
			for i in range(self.vertices):
				if len(self.graph[i]) % 2 != 0:
					odd += 1
			
			if odd == 0:
				return 2
			elif odd == 2:
				return 1
			elif odd > 2:
				return 0
        
