class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
def find_min_recursive(root):
    if root.left is None:
        return root
    else:
        return find_min_recursive(root.left)
def find_min_iterative(root):
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root
def find_max_recurisve(root):
    if root.right is None:
        return root
    else:
        return find_max_recurisve(root.right)
def find_max_iterative(root):
    if root is None:
        return None
    while root.right is not None:
        root = root.right
    return root
def insert_recursively(root,data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                insert_recursively(root.left,data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                insert_recursively(root.right,data)
    
root = None
root = insert_recursively(root, 50)  
insert_recursively(root, 30)  
insert_recursively(root, 20)  
insert_recursively(root, 40)  
insert_recursively(root, 70)  
insert_recursively(root, 60)  
insert_recursively(root, 80)