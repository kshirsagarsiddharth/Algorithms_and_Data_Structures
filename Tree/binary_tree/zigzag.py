class Node:  
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

"""
def zig_zag(root):
    if root is None:
        return
    
    current = []
    Next = []
    # pushing the root
    current.append(root)

    # direction of the variable
    is_left_right = True

    while len(current)!= 0:
        temp = current.pop()
        print(temp.data)

        if is_left_right is True:
            if temp.left is not None:
                Next.append(temp.left)
            if temp.right is not None:
                Next.append(temp.right)

        else:
            if temp.right is not None:
                Next.append(temp.right)
            if temp.left is not None:
                Next.append(temp.left)
        
        if len(current) == 0:
            is_left_right = not is_left_right
            current.Next = Next,current
"""
def zig_zag_traversal(root):
    current = []
    next_s = []
    current.append(root)
    is_left = True
    while len(current) != 0:
        temp = current.pop()
        print(temp.data)
        if is_left is True:
            if temp.left is not None:
                next_s.append(temp.left)
            if temp.right is not None:
                next_s.append(temp.right)
        else:
            if temp.right is not None:
                next_s.append(temp.right)
            if temp.left is not None:
                next_s.append(temp.left)
    
        if len(current) == 0:
            current,next_s = next_s,current
            is_left = not is_left

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(7) 
root.left.right = Node(6) 
root.right.left = Node(5) 
root.right.right = Node(4) 
zig_zag_traversal(root)         

        

