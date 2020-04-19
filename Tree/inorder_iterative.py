"""
Iterative Inorder Traversal Algorithm
1 -- > Create an empty stack
2 -- > Initialize the curent node as the root
3 -- > Push the current node to the stack and set current = current.left until the current node is NULL
4 -- > If the current node is NULL and the stack is not empty
        1 ----) Pop the top item from the stack
        2 ----) Print the popped item and set current = popped_item.right
        3 ----) go to  step 3 -- > 
5 -- > If current  is NULL and the stack is empty we are done
"""

# python program to perform iterative inorder traversal
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def iterative_inorder(root):

    # set current to root of binary tree
    current = root
    # stack initialization
    stack = [] 

    while True:

        # reach the leftmost node of the current node in the stack
        if current is not None:
            stack.append(current)
            current = current.left

        elif len(stack) != 0:
            current = stack.pop()
            print(current.data)

            current = current.right
        
        else:
            break


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print(iterative_inorder(root))
