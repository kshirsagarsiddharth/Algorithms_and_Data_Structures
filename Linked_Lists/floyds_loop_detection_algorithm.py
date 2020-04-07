'''
Algorithm

Traverse the linked list using two pointers
Move one pointer (slow_p) by one and another pointer(fast_p) by two.
If this pointers meet there is a loop or there is no loop in the linked list . 
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
        
    def detect_loop_floyd(self):
        slow_ptr = self.head
        fast_ptr = self.head
        
        while(slow_ptr and fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = slow_ptr.next.next
            
            if slow_ptr == fast_ptr:
                print('loop found')
                return
        return False
    
    
        