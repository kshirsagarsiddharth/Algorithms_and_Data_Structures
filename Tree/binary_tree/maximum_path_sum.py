class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

max_sum = 0 
def max_path_sum(root):
    global max_sum
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return root.data
    
    l = max_path_sum(root.right)
    r = max_path_sum(root.left)

    max_one = max(root.data,root.data + max(l,r))
    max_two = max(max_one,l + r + root.data)

    max_sum = max(max_sum,max_two)

    return max_one
root = Node(10) 
root.left = Node(2) 
root.right   = Node(10)
root.left.left  = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left   = Node(3)
root.right.right.right  = Node(4)
max_path_sum(root)