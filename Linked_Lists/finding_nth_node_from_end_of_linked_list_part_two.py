# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 02:30:25 2020

@author: siddharth
"""
'''Algorithm for this operation using two nodes
 
 maintain two pointers reference pointers and main pointer
 Initialize both main pointer and reference pointers to head
 first move reference pointer to n nodes from head.
 now move both pointers one by one until the reference pointer reaches the end
 now the main pointer will point the nth node from the end
 '''
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
        
    def print_nth_node_from_last_2ptrs(self,n):
        temp = self.head
        main_ptr  = self.head
        ref_ptr = self.head
        
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
        
        if n > length:
            print('Location is greater than number of nodes in the linked list')
            
            return
        
        for i in range(0,n):
            ref_ptr = ref_ptr.next
            
        while(ref_ptr is not None):
            main_ptr = main_ptr.next
            ref_ptr = ref_ptr.next
        print(main_ptr.data,n)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        