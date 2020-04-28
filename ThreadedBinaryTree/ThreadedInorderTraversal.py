class ThreadedBinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.l_tag = None
        self.right = None
        self.r_tag = None

# if P has no right subtree than return the right chhild of P. if P has right subtree , 
# than return the left of the nearest node whose 
# left subtree contains P.
def inorder_sucessor(node):
    if node.r_tag == 0:
        return node.right
    else:
        position = node.right
        while position.l_tag == 1:
            position = position.left
        return position

# To inorder traverse the threaded binary tree we start from the dummy node.And perform inorder traversal, until we encounter the dummy node again.
def threaded_inorder(root):
    P = root
    while True:
        P = inorder_sucessor(P)
        if P == root:
            return 
        return P.data

