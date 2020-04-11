# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 06:19:55 2020

@author: siddharth
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



    
class Stack:
    def __init__(self,data = None):
        self.head = None
    # check if the stack is empty   
    
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
        
    # method for adding data to the stack
    def push(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            # removes the head node and makes the 
            # preeciding node as head
            pop_node = self.head
            self.head = self.head.next
            pop_node.next = None
            
            return pop_node.data
        
    def print_stack(self):
        if self.is_empty():
            print('stack underflow')
        else:
            current = self.head
            while(current is not None):
                print(current.data)
                current = current.next
        

st = Stack()    

st.push(6)
print(st.is_empty())      
            