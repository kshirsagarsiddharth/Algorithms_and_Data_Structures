class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

def structurally_identical_trees(root1,root2):
    if (not root1.left and not root1.right and not root2.left and not root2.right) and (root1.data == root2.data):
        return True
    
    if (root1.data != root2.data) or (root1.left and not root2.left) or (not root1.left and root2.left) or (not root1.right and root2.right) or (root1.right and not root2.right):
        return False
    
    left = structurally_identical_trees(root1.left,root2.left) 
    right = structurally_identical_trees(root1.right,root2.right) 

    return left and right

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root1 = Node(1) 
root1.left = Node(2) 
root1.right = Node(3) 
root1.left.left = Node(4) 
root1.left.right = Node(5)
root1.left.right = Node(56)  
structurally_identical_trees(root1,root)