# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 03:30:56 2020

@author: siddharth
"""

'''Algorithm to find loop in linked list using hashing

traverse the list one by one and keep putting the node address in the 
hash table.

At any point in the traversal if NULl is rteached return false 

and if next of current node points to any of the previously stored nodes in the
hash than return true
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def insert_node_at_beginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def print_linked_list(self):
        temp = self.head
        while(temp):
            print(temp.data,end  = ' ')
            temp = temp.next
    
    def detect_loop(self):
        s = set()
        temp = self.head
        # if we already have this node in hash map
        # this tells us that there is a cycle
        while(temp):
            if temp in s:
                return True
            # if we have not encountered this element before we add it to the hash function
            s.add(temp)
            temp = temp.next
        return False
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        