# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 10:10:07 2020

@author: siddharth
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_from_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


def print_linked_list(linked_list):
    temp = linked_list
    while (temp):
        print(temp.data)
        temp = temp.next
      
# code to insert additional nodes in between the list
def cloning_with_random_pointers(selfe):
   current = selfe
   while current is not None:
       new = Node(current.data)
       new.next = current.next
       current.next = new
       current = current.next.next
       
   current = selfe
   # adjusting the random nodes of the linked list
   while(current is not None):
       current.next.random = current.random.next
       current = current.next.next
   
   # detach the original and duplicate from each other
   current = selfe
   
   while(current is not None):
       copy = current.next
       current.next = current.next.next
       curent = copy
   return current
           

       
    # 1's random points to 3 
    
        
####### Driver code ####### 
'''Create a doubly linked list'''
original_list = Node(1) 
original_list.next = Node(2) 
original_list.next.next = Node(3) 
original_list.next.next.next = Node(4) 
original_list.next.next.next.next = Node(5) 

'''Set the random pointers'''

# 1's random points to 3 
original_list.random = original_list.next.next

# 2's random points to 1 
original_list.next.random = original_list 

# 3's random points to 5 
original_list.next.next.random = original_list.next.next.next.next

# 4's random points to 5 
original_list.next.next.next.random = original_list.next.next.next.next

# 5's random points to 2 
original_list.next.next.next.next.random = original_list.next          
    
           
           