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
        
        def print_ssc(self):
            


