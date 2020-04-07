# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 06:03:33 2020

@author: siddharth
"""

#
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

    def reverse_ll(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        
    def reverse_linkled_list_iteratively(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        
            
        
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    