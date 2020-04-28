class ThreadedBinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.l_tag = None
        self.right = None
        self.r_tag = None


def pre_order_sucessor(node):
    if node.l_tag == 1:
        return node.left
    else:
        position = node
        while(position.r_tag == 0):
            position = position.right
        return position.right

        
def threaded_preorder_traversal(dummy):
    P = dummy
    while True:
        P = threaded_preorder_traversal(P)
        if P == dummy:
            return
        return P.data


