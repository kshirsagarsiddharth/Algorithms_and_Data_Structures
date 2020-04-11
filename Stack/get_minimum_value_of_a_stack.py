# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 07:57:56 2020

@author: siddharth
"""

class SmartStack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.stack_array = []
        self.min_array = []
        
    def stack_minimum(self):
        return self.min_array[-1]
    
    def smart_push(self,x):
        self.stack_array.append(x):
            if x <= stack_minimum():
                self.min_array.append(x)
            else:
                self.min_array.append(self.min_array[-1]) 
    def smart_pop(self):
        x = self.stack_array.pop()
        self.min_array.pop()
        return x
            
class SmartStack_one:
    def __init__(self,capacity):
        self.capacity = capacity
        self.original = []
        self.min = []
        
    def stack_minimum(self):
        return self.min[-1]
    
    def smart_push(self,x):
        self.original.append(x)
        if x <= stack_minimum():
            self.min.append(x)
        else:
            self.min.append(self.min[-1])
    
    def smart_pop(self):
        x = self.original.pop()
        self.min.pop()
        return x
    
class SmartStack_two:
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.original = []
        self.min = []
        
    def stack_minimum(self):
        return self.min[-1]
    
    def smart_push(self,x):
        self.original.append(x)
        if x <= stack_minimum():
            self.min.append(x)
            
    def smart_pop(self):
        x = self.original.pop()
        if x == stack_minimum():
            self.min.pop()
        return x