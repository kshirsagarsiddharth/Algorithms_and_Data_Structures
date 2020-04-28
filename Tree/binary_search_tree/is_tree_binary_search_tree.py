class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
INT_MIN = -9999999999999
INT_MAX = 99999999999999
def is_subtree_greater(root,value):
    if root is None:
        return True
    if root.data > value and is_subtree_greater(root.left,value) and is_subtree_greater(root.right,value):
        return True
    else:
        return False

def is_subtree_smaller(root,value):
    if root is None:
        return True
    if root.data < value and is_subtree_smaller(root.left,value) and is_subtree_smaller(root.right,value):
        return True
    else:
        return False

def is_binary_search_tree(root):
    if root is None:
        return True
    if is_subtree_smaller(root.left,root.data) and is_subtree_greater(root.right,root.data) and is_binary_search_tree(root.left) and is_binary_search_tree(root.right):
        return True
    else:
        return False

def is_binary_search_tree_efficient(root,min_val,max_val):
    if root == None:
        return True
    if root.data > min_val and root.data < max_val and is_binary_search_tree_efficient(root.left,min_val,root.data) and is_binary_search_tree_efficient(root.right,root.data,max_val):
        return True
    else:
        return False

def is_binary_search_tree_efficient_call(root):
    return is_binary_search_tree_efficient_call(root,INT_MIN,INT_MAX)
prev = None
def is_binary_tree_iterative(root):
    
