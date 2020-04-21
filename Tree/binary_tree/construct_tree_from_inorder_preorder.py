class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

pre_index = 0

def find_index(array,start,end,value):
    for i in range(start,end + 1):
        if array[i] == value:
            return i

def build_tree(in_order,pre_order,start,end):
    global pre_index

    if start > end:
        return None
    
    root = Node(pre_order[pre_index])
    pre_index += 1

    if start == end:
        return root
    
    in_index = find_index(in_order,start,end,root.value)

    root.left = build_tree(in_order,pre_order,start,in_index - 1)
    root.right = build_tree(in_order,pre_order,in_index + 1,end)
    return root

"""
pre_index = 0

def find_index(array,start,end,value):
    for i in range(start,end + 1):
        if array[i] == value:
            return i

def build_tree(inorder,preorder,start,end):
    global pre_index
    root = Node(preorder[0])
    pre_index += 1
    if start > end:
        return None

    if start == end:
        return root
    in_index = find_index(inorder,start,end,root)
    root.left = build_tree(inorder,preorder,start,in_index - 1)
    root.right = build_tree(inorder,preorder,start,in_index + 1)

    return root
"""


































