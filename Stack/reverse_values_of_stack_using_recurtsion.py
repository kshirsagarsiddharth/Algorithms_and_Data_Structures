# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 01:01:41 2020

@author: siddharth
"""
# reversing the values of the stack using recursion




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
    
    # recursive function that inserts at the bottom of the stack
    
    def insert_at_bottom(self,item):
        if self.is_empty():
            self.push(item)
        else:
            temp = self.pop()
            self.insert_at_bottom(item)
            self.push(temp)
            
    def reverse(self):
        if not self.is_empty():
            temp = self.pop()
            self.reverse()
            self.insert_at_bottom(temp)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    