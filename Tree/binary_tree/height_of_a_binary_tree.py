class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

'''
The diameter of a tree can be largest in the following
the diameter of Trees left subtree 
the diameter of Trees right subtree
The longest path between leaves that goes through the root of T
'''

def height_of_tree(root):
    return (height_of_tree(root.left) + 1 + height_of_tree(root.right))