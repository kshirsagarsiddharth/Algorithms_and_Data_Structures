
class Node:
    def __init__(self,new_data):
        self.data = new_data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_value_at_beginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        