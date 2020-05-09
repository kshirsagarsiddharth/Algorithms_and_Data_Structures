# detect a cycle in undirected graph

from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[v].append(u)
        self.graph[u].append(v)
    # this function used visited and parent to detect cycle in subgraph reachable from vertex v.
    def is_cyclic_util(self,v,visited,parent):

        # mark the current node as visited
        visited[v] = True

        # recur for all vertices adjcent to this vertex
        for i in self.graph[v]:
            # if the node is not visited recurse on that node
            if visited[i] == False:
                if self.is_cyclic_util(i,visited,v) == True:
                    return True
            # if an adjcent vertex is visited and not parent of current vertex then there is a cycle

            elif parent != i:
                return True
        
        return False

    # this function returns truw if the graph contains a cycle, else false.

    def is_cyclic(self):
        # mark all the vertices as not visited

        visited = [False] * self.vertices

        # call the recursive helper function to detect the cycle in different dfs trees

        for i in range(self.vertices):
            if visited[i] == False:
                # dont recur for the node which is already visited

                if self.is_cyclic_util(i,visited,-1) == True:
                    return True
        
        return False



from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    
    def is_cyclic_util(self,v,visited,parent):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                if self.is_cyclic_util(i,visited,v) == True:
                    return True
                
                elif parent != i:
                    return True 
        return False
    
    def is_cyclic(self):
        visited = [False] * self.vertices
        parent = -1
        for i in range(self.vertices):
            if visited[i] == False:
                if self.is_cyclic_util(i,visited,parent) == True:
                    return True
        return False

