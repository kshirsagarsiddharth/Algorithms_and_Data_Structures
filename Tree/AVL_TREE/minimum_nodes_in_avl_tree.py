def AVLnode(height):
    if height == 0:
        return 1
    elif height == 1:
        return 2


    return (1 + AVLnode(height - 1) + AVLnode(height - 2))

def rangeCount(root,a,b):
    if root == None:
        return 0
    elif root.data > b:
        return rangeCount(root.left,a,b)
    elif root.data < 1:
        return rangeCount(root.right,a,b)
    elif root.data >= a and root.data <= b:
        return rangeCount(root.left,a,b) + rangeCount(root.right,a,b) + 1