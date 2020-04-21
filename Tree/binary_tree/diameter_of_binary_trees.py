class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
""" Diameter of a binary tree is number of nodes on the longest path between two leaves of a tree"""
ptr = 0
def diameter_of_tree(root):
    global ptr
    if root is None:
        return 0
    left = diameter_of_tree(root.left)
    right = diameter_of_tree(root.right)

    if left + right > ptr:
        ptr = left + right
    
    return max(left,right) + 1