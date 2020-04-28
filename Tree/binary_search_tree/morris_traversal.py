class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def morris_traversal(root):
    current = root
    while current is not None:
        if current.left is None:
            print(current.data)
            current = current.right
        else:
            # find the inorder predecessor of current
            pre = current.left
            while(pre.right is not None and pre.right != current):
                pre = pre.right

            
            # make current as right child of its inorder predecessor
            if pre.right is None:
                pre.right = current
                current = current.left


            # revert the changes made
            else:
                pre.right = None
                print(current.data)
                current = current.right
