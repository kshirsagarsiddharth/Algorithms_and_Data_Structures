def prun_the_bst(root,Min,Max):
    if root is None:
        return None
    root.left = prun_the_bst(root.left)
    root.right = prun_the_bst(root.right)

    if root.data < Min:
        rchild = root.right
        return rchild
    
    if root.data > Max:
        lchild = root.left
        return lchild
    
    return root
        