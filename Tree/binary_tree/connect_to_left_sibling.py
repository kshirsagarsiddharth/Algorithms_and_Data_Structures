class Node:
    def __init__(self,data):
        self.next_sibling = None
        self.left = None
        self.right = None
def fill_next_sibling(root):
    if root is None:
        return None
    queue = []
    queue.append(root)
    sibling = None
    count = 0
    while len(queue) > 0:
        temp = queue.pop(0)
        #if len(queue) == 0:
        #    temp.next_sibling = None
        #else:
        temp.next_sibling = queue[0]
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
fill_next_sibling(root)