# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 03:36:29 2020

@author: siddharth
"""

# implementing stack using arrays

class Stack:
    
    def __init__(self,limit = 10):
        self.stk = limit * [None]
        self.limit = limit
   
    def is_empty(self):
        return len(self.stk) <= 0
    
    def push(self,item):
        if len(self.stk) > self.limit:
            self.resize()
        self.stk.append(item)
    
    def peek(self):
        if len(self.stk) < 0:
            print('stack underflow')
            return 0
        else:
            return self.stk[-1]
    
    
    def resize(self):
        new_stk = list(self.stk)
        self.limit = 2 * self.limit
        self.stk = new_stk
    def size(self):
        return len(self.stk)
    
            
        
        
            