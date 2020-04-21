class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def print_reverse_level_order(root):
    stack = []
    queue = []
    queue.append(root)
    while len(queue) != 0:
        temp = queue.pop(0)
        stack.append(temp.data)
        if temp.right is not None:
            queue.append(temp.right)
        if temp.left is not None:
            queue.append(temp.left)
    
    while len(stack) != 0:
        print(stack[-1])
        stack.pop()

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print_reverse_level_order(root)