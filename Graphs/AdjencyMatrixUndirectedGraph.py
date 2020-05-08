class UndirectedGraph:
    def __init__(self,num_nodes):
        self.adjacency_matrix = []
        for i in range(num_nodes):
            self.adjacency_matrix.append([0 for i in range(num_nodes)])
        self.num_nodes = num_nodes

    def add_edge(self,start,end):
        if start == end:
            print("{} and {} are the same vertex".format(start,end))
        self.adjacency_matrix[start][end] = 1
        self.adjacency_matrix[end][start] = 1

    def remove_edge(self,start,end):
        if self.adjacency_matrix[start][end] == 0:
            print("There is no edge between {} and {}".format(start,end))
        else:
            self.adjacency_matrix[start][end] = 0
            self.adjacency_matrix[end][start] = 0

    def contains_edge(self,start,end):
        if self.adjacency_matrix[start][end] > 0:
            return True
        else:
            return False
    def __len__(self):
        return self.num_nodes
