# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 02:08:26 2020

@author: siddharth
"""

'''Algorithm

1) In the linked list is empty than make the node as head and return it

2)If the value of the node to be inserted is smaller than the head node, 
than insert the node at start and make the node as head node.

3)In a loop, find the appropriate node after which the input node is to
be inserted to find the appropriate node start from the head, keep moving 
until you reach a node whose value is greater than the input node the node 
just before the former node is appropriate node

4)Insert the node after appropriate found in step 3 
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
    
    def insert_sorted_way_with_node(self,new_node):
        
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while(current.next is not None and current.data < new_node.data):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
    
    def insert_sorted_way_with_data(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while(current.next is not None and current.data < new_node.data):
                current = current.next
                
            new_node.next = current.next
            current.next = new_node
            
        
                
    
    
            
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    