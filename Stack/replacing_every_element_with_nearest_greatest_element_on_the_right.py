# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 08:17:05 2020

@author: siddharth
"""



# brute force approach                
array = [16, 17, 4, 3, 5, 2,3] 
for i in range(0,len(array) - 1):
    for j in range(i + 1,len(array)):
        if array[i] < array[j]:
            array[i] = array[j]             
            
# optimal approach
arr = [16, 17, 4, 3, 5, 2] 
size = len(arr)
# initializing the next greatest element
max_from_right = arr[size - 1]
# the next greatest element from the rightmost side is always -1
arr[size - 1] = -1

    
for i in reversed(range((size - 1))):
               temp = arr[i]
               
               arr[i] = max_from_right
               
               if max_from_right < temp:
                   max_from_right = temp