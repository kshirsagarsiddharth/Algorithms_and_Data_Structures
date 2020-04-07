# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 07:06:53 2020

@author: siddharth
"""

'''
Algorithm to print elements of linked list in a recursive way

1. seperate the list into two pieces The first node(head) and the 
rest of nodes (called tails)

2. print the tail backwards

3. print the head
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    
        
    def print_linked_list_from_end(self,linked_list):
        if linked_list.head == None:
            print('The linked list is not defined')
            return
        head_node = linked_list.head
        tail_node = linked_list.head.next
        self.print_linked_list_from_end(tail_node)
        print(head_node.data)