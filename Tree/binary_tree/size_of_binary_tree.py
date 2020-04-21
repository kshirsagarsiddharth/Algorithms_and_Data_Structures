class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
def recursive_size(root):
    if root is None:
        return 0
    else:
        left_size = recursive_size(root.left)
        right_size = recursive_size(root.right)
        return left_size + right_size + 1
def iterative_size(root):
    if root is None:
        return 0
    queue = []
    queue.append(root)
    count = 1
    while(len(queue) != 0):
        temp = queue.pop(0)
        if temp.left is not None:
            queue.append(temp.left)
            count += 1
        if temp.right is not None:
            queue.append(temp.right)
            count += 1



root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
recursive_size(root)







































