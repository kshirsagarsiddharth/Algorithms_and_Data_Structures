class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

# printing ancestors of a given node in a binary tree

# if the target is present in the tree than print the ancestors of the 
# tree and return true else return false

def print_ancestors(root,target):
    if root == None:
        return False
    
    if root.data == target:
        return True

    # if the target is present in the left or right sub tree
    # of this node than print that node
    left = print_ancestors(root.left,target)
    right = print_ancestors(root.right,target)
    if left or right:
        print(root.data)
        return True
    
    return False
"""
def print_ancestors_of_tree(root,target):
    if root is None:
        return False
    if root == target:
        return True
    
    left = print_ancestors_of_tree(root.left,target)
    right = print_ancestors_of_tree(root.right,target)
    if left or right:
        print(root.data)
        return True
    return False
"""