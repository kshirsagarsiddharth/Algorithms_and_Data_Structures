# program to find bridges in an undirected graph
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
    A recursive function that finds and prints bridges in a graph using DFS traversal

    u -- The vertex to be visited next
    visited -- keeps rack of visited vertices
    disc -- stores discovery time of visited vertex
    parent -- stores parent vertices in DFS tree
    """

    def bridge_util(self,u,visited,parent,low,disc):
        # mark curent node as visited and print it
        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        # recur for all the vertices adjcent to this vertices
        for v in self.graph[u]:
             # if v is not visited yet, than make it the children of u
             # in dfs tree recur for it
            
            if visited[v] == False:
                 parent[v] = u
                 self.bridge_util(v,visited,parent,low,disc)

                 # check if subtree rooted with v has a connection to one of the ancestors of u
                 low[u] = min(low[u],low[v])

                 """
                 if the lowest vertex reachable from subtree under v is below u in the dfs tree than u - v is a bridge
                 """ 
                 
                 if low[v] > disc[u]:
                     print("{},{}".format(u,v))

            elif v != parent[u]:
                low[u] = min(low[u],disc[v])

    # DFs based function to find all the bridges. 

    def bridge(self):
        visited = [False] * self.vertices
        disc = [float("inf")] * self.vertices
        low = [float("inf")] * self.vertices
        parent = [-1] * self.vertices

        for i in range(self.vertices):
            if visited[i] == False:
                self.bridge_util(i,visited,parent,low,disc)


