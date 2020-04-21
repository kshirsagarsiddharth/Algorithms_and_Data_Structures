class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def iterative_post_order_two_stacks(root):
    if root is None:
        return
    # create two stacks
    stack_one = []
    stack_two = []

    # push the root to the first stack
    stack_one.append(root)

    # run while the stack is not empty
    while len(stack_one) != 0:
        # pop an item from stack_one and append
        # the item to stack_two
        node = stack_one.pop()
        stack_two.append(node)

        #push the left and right elements of the popped
        # stack to stack_one
        if node.left is not None:
            stack_one.append(node.left)
        if node.right is not None:
            stack_one.append(node.right)
    
    while len(stack_two) != 0:
        node = stack_two.pop()
        print(node.data)



result = []
def iterative_post_order_one_stack(root):
    if root is None:
        return
    
    stack = []

    while True:

        while root is not None:
            # push the roots right chile and than the root onto the stack
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)

            # set the root is roots left child
            root = root.left

        # pop item from the stack and set it as root
        root = stack.pop()
        # if the popped item has a right child and the right child is
        # at the top of the stack then remove the rigtht child from the stack
        # push the root back and set the root as the roots right child
        if root.right is not None and stack[-1] == root.right:
            stack.pop() # remove the right child from the stack
            stack.append(root) # push the root back to the stack
            root = root.right # change the root as the right child of the 
            # root

        # else print the roots data and set the root as None
        else:
            result.append(root.data)
            root = None
        
        if len(stack) <= 0:
            break

def post_order_recursive(root):
    if root  == None:
        return
    post_order_recursive(root.left)
    post_order_recursive(root.right)
    print(root.data)
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 

