def remove_nodes_with_only_one_child(root):
    if root is None:
        return 
    root.left = remove_nodes_with_only_one_child(root.left)
    root.right = remove_nodes_with_only_one_child(root.right)

    if root.left is None and root.right is None:
        return root
    if root.left is None:
        return root.right
    if root.right is None:
        return root.left
    
    return root