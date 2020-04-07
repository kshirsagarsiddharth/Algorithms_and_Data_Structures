# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 01:38:43 2020

@author: siddharth
"""

# finding n th node from end of linked list
class Node:
    def __init__(self,new_data):
        self.data = new_data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    # function to insert new node from beginning
    def insert_value_beginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def print_nth_node_from_last(self,n):
        temp = self.head
        
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
            
        if n > length:
            print('Location is greater than length of the linked list')
            
            return
        temp = self.head
        for i in range(0,length - n):
            temp = temp.next
        print(temp.data)
    
    
    

cla