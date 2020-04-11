# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 01:40:29 2020

@author: siddharth
"""
# brute force approach
def calculate_span_bruteforce(price):
    span = [None] * len(price)
    span[0] = 1  # the span value of first day is always one
     # now we calculate the span value of remaning days by linearly
    # checking previous values
    for i in range(1,len(price)):
        span[i] = 1
        j = i - 1
        # initializing the span values
        # traverse left while the next element on left is
        # smaller than price[i]
        while j >= 0 and price[i] > price[j]:
            span[i] += 1
            j -= 1
        
    return span
# linear time solution for stack span problem
def calculate_span_efficiently(price,S):
    n = len(price)
    S[0] = 1
    st = []
    st.append(0)
    for i in range(1,n):
        while(len(st) >  0 and price[st[-1]] <= price[i]):
            st.pop()
        if len(st) <= 0:
            S[i] = i + 1
        else:
            S[i] = i - st[-1]
        
        st.append(i)


       

      
    


