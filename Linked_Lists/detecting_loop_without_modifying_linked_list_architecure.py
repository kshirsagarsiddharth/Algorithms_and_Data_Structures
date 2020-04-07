
'''
Algorithm for marking visited node without modifying the linked list data structure

In this method a temporary node is created .The next pointer of each node traversed is made to point to the temporary node

this way we are using next pointer of the node as a flag to indicate wether the node is traversed or not

every node is checked to see if the next is pointing to a temp node or not

In case of first node of the loop, the second time we traverse it this condition will be true, hence we find that loop exists

if we come accross a node that points to null than the loop doesnot exist. 
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_from_beginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def print_linked_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def detect_loop_without_changing_ll_ds(self):
        head_node = self.head
        temp = ' '
        while(head_node)
            if head_node.next == temp:
                return True
            
            nex = head_node.next
            head_node.next = temp
            
            head = nex
        return False
        
        
        
            
            
        
        