class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def find_recursive(root,data):
    if root is None:
        return 0
    if root.data == data:
        return 1
    
    else:
        temp = find_recursive(root.left,data)
        if temp == 1:
            return temp
        else:
            return find_recursive(root.right,data)

def find_iteratively(root,data):
    if root is None:
        return -1
    queue = []
    queue.append(root)
    node = None
    while len(queue) != 0:
        node = queue.pop(0)
        if data == node.data:
            return 1
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return 0

root = Node(2) 
root.left = Node(7) 
root.right = Node(5) 
root.left.left = Node(8)
root.left.right = Node(9)
root.right.left = Node(10)
root.right.right = Node(11)
find_iteratively(root,9)
