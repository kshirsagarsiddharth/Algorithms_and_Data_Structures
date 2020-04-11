# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 04:40:26 2020

@author: siddharth
"""
'''Algorithm

1)create a stack to store operands or values

2) scan the given elements and do the followinf for every scanned elements
    1) if the element is a number push it onto the stack
    2) if the elements is a operator, pop operands for the 
    operator from the stack. evaluate the result and push back onto the 
    stack
3) when the expression is ended, the number in the stack is the final solution
'''

class EvaluatePostfix:
    
    def __init__(self,capacity):
        self.top = -1
        self.capacity = capacity
        # this array is used as a stack
        self.array = []
        
    def is_empty(self):
        return True if self.top == -1 else False
    
    def peek(self):
        return self.array[-1]
    
    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.array.pop()
        else:
            return False
        
    def push(self,operands):
        self.top += 1
        self.array.append(operands)
        
    def evaluate_postfix(self,expression):
        for i in expression:
            
            if i.isdigit():
                self.push(i)
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))
        return int(self.pop())


exp = "2 3 1 * + 9 -".split()
st = EvaluatePostfix(100)
print(st.evaluate_postfix(exp))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    