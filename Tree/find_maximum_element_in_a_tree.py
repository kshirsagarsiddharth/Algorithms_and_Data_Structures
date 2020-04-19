# python recursive code to find the maximum element in a binary tree

class newNode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def find_max_iteratively(root):
    queue = []
    queue.append(root)
    max_val = 0
    while(len(queue) > 0):
        temp = queue.pop(0)
        if temp.data > max_val:
            max_val = temp.data
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)
    return max_val
max_data = float("-inf")
def find_max_recursively(root):
    global max_data
    if not root:
        return max_data
    if root.data > max_data:
        max_data = root.data
    find_max_recursively(root.left)
    find_max_recursively(root.right)
    return max_data
root = newNode(2) 
root.left	 = newNode(7) 
root.right	 = newNode(5) 
root.left.right = newNode(6) 
root.left.right.left=newNode(1) 
root.left.right.right=newNode(11) 
root.right.right=newNode(9) 
root.right.right.left=newNode(4)
find_max_recursively(root)
