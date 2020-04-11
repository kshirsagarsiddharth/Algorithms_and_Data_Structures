# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 09:02:55 2020

@author: siddharth
"""


def check_validity(to_push,to_pop):
    stack = []
    j = 0
    for x in to_push:
        stack.append(x)
        while stack and j < len(to_pop) and stack[-1] == to_pop[j]:
            stack.pop()
            j = j + 1
    return j == len(to_pop)
        
        
pushed = [1, 2, 3, 4, 5] 
popped = [4, 5, 3, 2, 1] 

print(check_validity(pushed,popped))

def check_validity(pushed,popped):
    stack = []
    j = 0
    for x in pushed:
        stack.append(x)
        while stack and len(popped) > j and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return j == len(popped)