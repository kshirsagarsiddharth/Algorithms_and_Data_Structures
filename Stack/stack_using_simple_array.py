# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 03:36:29 2020

@author: siddharth
"""

# implementing stack using arrays

class Stack:
    
    
    # creating stack class and initializing the constructor
    def __init__(self,limit = 10):
        self.stk = []
        self.limit = limit
    # this function returns True if the stack(array) is empty else this 
    # function returns true
    def is_empty(self):
        return len(self.stk) <= 0
    
    def push(self,item):
        if len(self.stk) > self.limit:
            print('stack overflow')
        else:
            self.stk.append(item)
        print('stack after push -- >',self.stk)
    
    def pop(self):
        if len(self.stk) < 0:
            print('stack underflow')
            return 0
        else:
            return self.stk.pop()
    def peek(self):
        if len(self.stk) < 0:
            print('stack underflow')
            return 0
        else:
            return self.stk[-1]
        
    def size(self):
        return len(self.stk)
            
        
        
            