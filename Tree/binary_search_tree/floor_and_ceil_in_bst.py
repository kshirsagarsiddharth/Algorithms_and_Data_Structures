INT_max = 3894379847389
class Node: 

	# Construct to create a newNode 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def insert(root,key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root

def floor_bst(root,key):
    """ floor is the greatest element smaller than or equal to x """

    if root is None:
        return INT_max

    if root.data == key:
        return root.data

    if root.data > key:
        return floor_bst(root.left,key)
    
    """else the floor may lie in the right subtree or may be equall to the 
    root
    """
    floor_value = floor_bst(root.right,key)

    return floor_value if floor_value <= key else root.data    

    
