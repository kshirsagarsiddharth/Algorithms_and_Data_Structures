# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 04:42:18 2020

@author: siddharth
"""
'''
Algorithm to find the largest area in a histogram
1) create a empty stack

2) start from the first bar, and do the folllowing for every bar 'hist[i]' where 'i' varies from zero to n - 1
    a) if the stack is empty or hist[i] is higher than the bar at top in the stack ,then push i on the stack.
    b) if this bar is smaller then the top of the stack, then keep removing the top of the stack while top of the stack is greater.
        let the removed bar be hist[tp] 
        calculate the rectangle area with hist[tp] as smallest ber. for the hist[tp] the left index is previous item and right index is i or (current index)

3) if the stack is not empty then one by one remove all bars from stack and do step 2.b for every removed bar
'''

# python program to find the maximum rectangular area in a histogram

def max_area_histogram(histogram):
    # this function calculates the maximum rectangular area under a 
    # given histogram with n bars
    
    # create a empty stack. The stack holds the indexes of the histogram
    # the bars stored in the stack are always in increasing order of their height/
    
    stack = []
    max_area = 0 # initialize the max area to zero
    
    # run through all bars of all the histograms
    index = 0
    
    while index < len(histogram):
        
        # if this bar is higher than
        # the bar on top of stacks push it on the 
        # stacks
        
        if (not stack) or histogram[stack[-1]] < histogram[i]:
            stack.append(index)
            index += 1
            
            # if this bar is lower than top of the stack.
            # than calculate area of the rectangle with 
            # stack top as the smallest
            # i is the right index and the left index is the 
            # top element in the stack before the current top 
            # is the right index
            
        else:
            top_of_the_stack = stack.pop()
            # calculate the area with 
            # histogram[top_of_stack] as the smallest bar
            if stack:
                area = (histogram[top_of_the_stack] * (index - stack[-1] - 1))
            else:
                area = histogram[top_of_the_stack] * index
            
            max_area = max(max_area,area)
            
    while stack:
         top_of_the_stack = stack.pop()
            # calculate the area with 
            # histogram[top_of_stack] as the smallest bar
            if stack:
                area = (histogram[top_of_the_stack] * (index - stack[-1] - 1))
            else:
                area = histogram[top_of_the_stack] * index
            
            max_area = max(max_area,area)
            
    return max_area