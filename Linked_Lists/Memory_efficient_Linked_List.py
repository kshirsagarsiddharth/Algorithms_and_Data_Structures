# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 03:27:28 2020

@author: siddharth
"""
# this is new node for memory efficient doubly linked list
class Node:
    # constructor
    def __init__(self):
        self.data = None
        self.ptrdiff = None
    # method for setting and getting the data field of the node
    
    def set_data(self,data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def set_ptr_diff(self,pev,next):
        self.ptrdiff = prev ^ next
    
    def get_ptr_diff(self):
        return ptrdiff
    
    
        
        

