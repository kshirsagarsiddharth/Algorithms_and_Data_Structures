def remove_root_node(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return None
    
    else:
        root.left = remove_root_node(root.left)
        root.right = remove_root_node(root.right)
    return root
    