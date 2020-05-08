# set up the matrix
class DirectedGraph:
    # a graph list completely filled with zeroes is generated when we create an instance of the class graph with help of below code.
    def __init__(self,num_nodes):
        self.adjacency_matrix = []
        for i in range(num_nodes):
            self.adjacency_matrix.append([0 for i in range(num_nodes)])
        self.num_nodes = num_nodes
        """
        the adjacency matrix looks like 
                        [[0, 0, 0, 0], 
                        [0, 0, 0, 0], 
                        [0, 0, 0, 0], 
                        [0, 0, 0, 0]]
        for number 4
        """
    def add_edge(self,start,end):
        self.adjacency_matrix[start][end] = 1
        """
        graph1 = Graph(4) # create an instance of the graph with 4 nodes
        graph1.add_edge(0,1) # the zeroth element is A and the 1st element is B this forms
        a node between zeroth node and the first node.

        [start] :  selects a row
        [end] : selects a column
        and the one is assigned to that position

        after this the adjacency matrix looks like
                        [[0, 1, 0, 0], # 0th row, 1st column.
                        [0, 0, 0, 0], 
                        [0, 0, 0, 0], 
                        [0, 0, 0, 0]]
        
        graph1.add_edge(0,2)
        graph1.add_edge(0,3)
        graph1.add_edge(2,3)

        """
    
    # remove edges we can also remove the edges from the graph consider wqe need to remove the edge between
    # vertex 2 and vertex 3. we use the below method this method checks wether there is a node between vertex 2 and vertex 3 i.e
    # there is one in 2 and 3

    def remove_edge(self,start,end):
        if self.adjacency_matrix[start][end] == 0:
            print("There is no edge between {} and {}".format(start,end))
        else:
            self.adjacency_matrix[start][end] = 0

    """we can also check if an edge exists by finding the element in the matrix and checking if it's 0 or 1. If the value of the edge is greater than zero, and edge exists and the method returns True. Otherwise, there is no edge between this nodes and the method returns False. """

    def contains_edge(self,start,end):
        if self.adjacency_matrix[start][end] > 0:
            return True
        else:
            return False

    def __len__(self):
        return self.num_nodes

"""
class DirectedGraph:
    def __init__(self,num_nodes):
        self.adjacency_matrix = []
        for i in range(num_nodes):
            self.adjacency_matrix.append([0 for i in range(num_nodes)])
        self.num_nodes = []


    def add_edge(self,start,end):
        self.adjacency_matrix[start][end] = 1
    
    def remove_edge(self,start,end):
        if self.adjacency_matrix[start][end] == 0:
            print("here is no edge between {} and {}".format(start,end))
        else:
            self.adjacency_matrix[start][end] = 0
    
    def contains_edge(self,start,end):
        if self.adjacency_matrix[start][end] > 0:
            return True
        else:
            return False
    
    def __len__(self):
        return self.num_nodes
        
"""