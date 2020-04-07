# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 03:23:01 2020

@author: siddharth
"""

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
            
    def is_palindrom(self):
        temp = []
        current = self.head
        while(current.next is not None):
            temp.append(current.data)
            current = current.next
        temp.append(current.data)
        string = ''.join((temp))
        
        if string == string[::-1]:
            return True
        else:
            return False
        
llist = LinkedList() 
llist.head = Node('a') 
llist.head.next = Node('bc') 
llist.head.next.next = Node("d") 
llist.head.next.next.next = Node("dcb") 
llist.head.next.next.next.next = Node("a") 