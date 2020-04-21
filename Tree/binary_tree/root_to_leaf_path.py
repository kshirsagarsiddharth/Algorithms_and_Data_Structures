class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def print_top_to_bottom_path(curr,parent):
    stack = []
    curr2 = 0
    # start from the leaf node and keep appending until the root node is
    # reached
    while curr is not None:
        stack.append(curr)
        curr = parent[curr]
    # start popping the nodes from the stack and print it
    while len(stack) != 0:
        curr = stack.pop()
        curr2 += curr.data
        print(curr.data)
    print(curr2)

def print_root_to_leaf(root):
    if root == None:
        return   
    # create a empty stack and append the root to it
    node_stack = []
    node_stack.append(root)
    parent = {}
    parent[root] = None
    # pop all the pointers and for each popped do the following
    # a) append its right child and set it as parent pointer
    # b) append its left child and set it as parent pointer
    while len(node_stack) != 0:
        current = node_stack.pop()
        if current.left is None and current.right is None:
            print_top_to_bottom_path(current,parent)
        if current.right is not None:
            parent[current.right] = current
            node_stack.append(current.right)
        if current.left is not None:
            parent[current.left] = current
            node_stack.append(current.left)

def print_root_to_leaf_rec(stack,root):
    if root == None:
        return
    # append this node to path array
    stack.append(root.data)
    if root.left is None and root.right is None:
        print([i for i in stack])
    print_root_to_leaf_rec(stack,root.left)
    print_root_to_leaf_rec(stack,root.right)
    stack.pop()
def print_root_to_leaf_rec(root,val):
    if root == None:
        return
    # append this node to path array
    val = (val * 10 + root.data)
    if root.left is None and root.right is None:
        return val
    val1 = print_root_to_leaf_rec(root.left,val)
    val2 = print_root_to_leaf_rec(root.right,val)
    return val1 + val2
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)
print_root_to_leaf_rec([],root)









