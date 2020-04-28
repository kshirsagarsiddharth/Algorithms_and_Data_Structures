def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left),height(root.right))

def is_balenced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)

    if (lh - rh) <= 1 and is_balenced(root.left) is True and is_balenced(root.right) is True:
        return True
    else:
        return False