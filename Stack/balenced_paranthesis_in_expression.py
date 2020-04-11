# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 07:10:29 2020

@author: siddharth
"""
'''
Declare a character stack S

Now traverse the string expression

if the current character is a starting paranthesis then push it onto the stack.

if the current character is the closing paranthesis than pop from the stack
if the popped character matches the starting bracket than it is good.
else the paranthesid are not balenced.

after travrersal if there are some opening paranthesis then the stack is not balenced
'''

# python program to check balance of paranthesis

def paranthesis_balence_checker(expression):
    s = []
    
    # traversing the expression
    for i in range(len(expression)):
        if expression[i] == '[' or expression[i] == '{' or expression[i] == '(':
            s.append(expression[i])
            continue
    
        # if current chaarecter is not opening than it will be closing
        # and the stack cannot be empty
        
        if(len(s) == 0):
            return False
        else:
        
            if expression[i] == ')':
                x = s.pop()
                if x == '{' or x == '[':
                    return False
            
            elif expression[i] == ']':
                x = s.pop()
                if x == '{' or x == '(':
                    return False
                
            elif expression[i] == '}':
                x = s.pop()
                if x == '(' or x == '[':
                    return False
                
    if len(s) == 0:
        return True
    else:
        return False
    print(s)   
                    
expr = "{ ( ) } [ ]".split()    


            
            
                            
            