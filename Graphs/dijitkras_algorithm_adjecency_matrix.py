"""
Dijkstra’s Algorithm

Given a graph and a source vertex in the graph, find the shortest path form the source to all the vertices in the graph.

We maintain two sets, one set contains vertices included in the shortest path tree, other set includes vertices not yet included in the shortest path tree. At every step of the algorithm, we find the vertices which are in the other set (set not yet included) and has a minimum distance from the source

ALGORITHM

1 -- Create a sptSet (shortest path tree set) that keeps track of vertices included in the shortest path of the tree
i.e whose minimum distance from source is calculated and finalized. This set is initally empty

2 -- Assign a distance valueto all the vertices in the input graph. Initialize all distance values as infinite. Assign distance value as 0 for source vertex so that it is picked up fist.

3 -- while sptSet dose not include all the vertices
    a - Pick a vertex "u" which is not there in sptSet and has minimumdistancevalue

     Include u to sptSet.
….c) Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex v, if sum of distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v.

"""
import sys 

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
    
    def print_solution(self,dist):
        print("Vertex diostance from the source")
        for node in range(self.vertices):
            print(node + " " + dist[node])
    
    # a utility function to find the vertex with minimum distance value, #from the set of vertices not yet included in the shortest path

    def min_distance(self,dist,spt_set):
        min = sys.maxsize

        for v in range(self.vertices):
            if dist[v] < min and spt_set[v] == False:
                min = dist[v]
                min_index = v
        return min_index
    

    def dijkstras(self,source):
        dist = [sys.maxint] * self.vertices
        dist[source] = 0
        spt_set = [False] * self.vertices

        for count in range(self.vertices):
            u = self.min_distance(dist,spt_set)

            spt_set[u] = True

            # update dist value of the adjcent vertices of the picked vertex only if the current distance is greater than new distance and the vertex is not in the shortest path tree

            for v in range(self.vertices):
                if self.graph[u][v] > 0 and spt_set[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
    

    

