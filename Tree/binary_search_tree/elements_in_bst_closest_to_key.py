import sys
import math
def closest_in_bst_iterative(root,key):
    difference = sys.maxsize
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        temp = queue.pop(0)
        if difference > abs(temp.data - key):
            difference = abs(temp.data - key)
            element = temp
        
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)






""" 
if the root is NULL than the closest value is zero

if the roots data match the given key then the closest is the root

else do the following:
    if the key is smaller than the root than find the key on the left side of the tree of the root recursively call it temp

    if the key is larger than root.data , find the closest on the right side of the root call it temp
return the root or temp depending on whichever is near to the given key.
"""


import math
import sys
def closest_to_bst(root,data):
    if root is None:
        return data

    if root.data == data:
        return root
    
    if data < root.data:
        if root.left is None:
            return root
        temp = closest_to_bst(root.left,data)
        if abs(temp.data - data) > abs(root.data - data):
            return root
        else:
            return temp
        
    else: # if data > root.data

        if root.right is None:
            return root
        temp = closest_to_bst(root.right,data)
        if abs(temp.data - data) > abs(root.data - data):
            return root
        
        else:
            return temp
    
    return None
    



    
