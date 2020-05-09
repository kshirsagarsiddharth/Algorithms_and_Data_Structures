
"""
ALGORITHM
1 --  Create a graph using given number of edges and vertices

2 -- create a recursive function with current index, visited array and recursion stack.

3 -- Mark the current node as visited and also mark the index in recursion stack.

4 -- Find all the vertices which are not visited and are adjcent to the current node. Recursive call the function for those nodes if the recursive function returns truue than return True.

5 -- If the adjcent vertices are already marked in the recursion stack than return true.
"""

from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices
    
    def add_edge(self,u,v):
        self.graph[u].append(v)

    def is_cyclic_util(self,v,visited,recu_stack):
        # mark current node as visited and add it to the stack
        visited[v] = True
        recu_stack[v] = True

        # recur for all the neighbors if any of the neighbor is visited and in the recursive stack than the graph is cyclic

        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.is_cyclic_util(neighbour,visited,recu_stack) == True:
                    return True
            elif recu_stack[neighbour] == True:
                return True
        # the node needs to be popped from the recursion stack before the function ends
        recu_stack[v] = False
        return False

    # this is the main function which returns True if there is a cycle in the graph
    def is_cyclic(self):
        visited = [False] * self.vertices
        recu_stack = [False] * self.vertices
        for i in range(self.vertices):
            if visited[i] == False:
                if self.is_cyclic_util(i,visited,recu_stack) == True:
                    return True
        return False

"""
from collections import defaultdict
class Graph:
	def __init__(self,vertices):
		self.graph = defaultdict(list)
		self.vertices = vertices

	def add_edge(self,u,v):
		self.graph[u].append(v)
	
	def is_cycle_util(self,v,visited,rec_stack):
		visited[v] = True
		rec_stack[v] = True

		for neighbour in self.graph[v]:
			if visited[neighbour] == False:
				if self.is_cycle_util(neighbour,visited,rec_stack) == True:
					return True
			elif rec_stack[neighbour] == True:
				return True
		
		rec_stack[v] = False
		return False

	def is_cycle(self):
		visited = [False] * self.vertices
		rec_stack = [False] * self.vertices

		for i in range(self.vertices):
			if visited[i] == False:
				if self.is_cycle_util(i,visited,rec_stack) == True:
					return True
		
		return False

"""