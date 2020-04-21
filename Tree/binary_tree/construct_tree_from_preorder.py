class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
"""        self.right = None
i = 0
def build_tree_from_preorder(A):
    global i
    if A == None or i >= len(A):
        return None
    new_node = Node(A[i])
    new_node.data = A[i]

    if A[i] == "L":
        return new_node
    i += 1
    new_node.left = build_tree_from_preorder(A)
    i += 1
    new_node.right = build_tree_from_preorder(A)

    return new_node
"""   
i = 0
def build_tree_from_preorder(A):
    if A is None or i >= len(A):
        return None
    new_node = Node(A[0])
    if A[i] == 'L':
        return new_node
    i+= 1
    build_tree_from_preorder(A)
    i+= 1
    build_tree_from_preorder(A)

    return new_node
