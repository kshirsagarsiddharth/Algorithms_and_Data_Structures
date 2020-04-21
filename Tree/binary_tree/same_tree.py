class Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

# this function returns true if the tree are structually identical

def identical_trees(root_a,root_b):
    # both trees are empty
    if root_a is None and root_b is None:
        return True
    # both are non empty compare them
    if root_a is not None and root_b is not None:
        return (root_a.data == root_b.data) and (identical_trees(root_a.left,root_b.left) and (identical_trees(root_a.right,root_b.right)))
    # one is empty and one is not
    return False

root1 = Node(1) 
root2 = Node(1) 
root1.left = Node(2) 
root1.right = Node(3) 
root1.left.left = Node(4) 
root1.left.right = Node(5) 
  
root2.left = Node(2) 
root2.right = Node(3) 
root2.left.left = Node(4) 
root2.left.right = Node(5) 

identical_trees(root1,root2)

