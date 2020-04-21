# performing iterative preorder traversal

# node of a binary tree
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def iterative_preorder_traversal(root):

    if root is None:
        return
    # create a empty stack and push root onto it
    stack = []
    stack.append(root)
    """
    do the following until the stack is not empty.
        1) pop an item from the stack and print it.
        2) push right child of popped item onto the stack.
        3) push left child of the popped item onto the stack.

    """
    while len(stack) != 0:
        # pop the top item and print it
        node = stack.pop()
        print(node.data)

        # push right and left elements of the popped 
        # nodes onto the stack
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)


