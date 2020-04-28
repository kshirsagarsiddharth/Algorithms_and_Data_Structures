class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def print_in_range_recursive(root,k1,k2):
    if root is None:
        return
    
    if root.data > k1:
        print_in_range_recursive(root.left,k1,k2)
    
    if root.data > k1 and root.data < k2:
        print(root.data)
    
    if root.data < k2:
        print_in_range_recursive(root.right,k1,k2)

def print_in_range_iterative(root,k1,k2):
    if root is None:
        return None
    queue = []
    queue.append(root)
    while len(queue) != 0:
        temp  = queue.pop(0)
        if temp.data < k1 and temp.data > k2:
            print(temp.data)
        
        if temp.left is not None and temp.data >= k1:
            queue.append(temp.left)
        if temp.right is not None and temp.data <= k2:
            queue.append(temp.right)

# printing range without iteration and recursion

def morris_traversal(root,k1,k2):
    current = root
    while current is not None:
        if current.left is None:
            if current.data <= k1 and current.data >= k2:
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
                if current.data <= k1 and current.data >= k2:
                    print(current.data)
                current = current.right






 