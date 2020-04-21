class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def find_leaf_nodes(root):
    if root is None:
        return 
    queue = []
    queue.append(root)
    count = 0
    while(len(queue) > 0):
        temp = queue.pop(0)
        if temp.right is None and temp.left is None:
            count += 1
        
        if temp.left is not None:
            queue.append(temp.left)
        
        if temp.right is not None:
            queue.append(temp.right)
        
    return count

def find_non_leaf_nodes(root):
    if root is None:
        return 
    queue = []
    queue.append(root)
    count = 0
    while(len(queue) > 0):
        temp = queue.pop(0)
        if temp.right is not None and temp.left is not None:
            count += 1
        
        if temp.left is not None:
            queue.append(temp.left)
        
        if temp.right is not None:
            queue.append(temp.right)
        
    return count

def find_half_nodes_in_a_tree(root):
    if root is None:
        return 
    queue = []
    queue.append(root)
    count = 0
    while(len(queue) > 0):
        temp = queue.pop(0)
        if (temp.right is None and temp.left is not None) or (temp.right is not None and temp.left is None):
            count += 1
        
        if temp.left is not None:
            queue.append(temp.left)
        
        if temp.right is not None:
            queue.append(temp.right)
        
    return count
root = Node(10) 
root.left = Node(11) 
root.left.left = Node(7) 
root.left.right = Node(12) 
root.right = Node(9) 
root.right.left = Node(15) 
root.right.right = Node(8) 

find_half_nodes_in_a_tree(root)

