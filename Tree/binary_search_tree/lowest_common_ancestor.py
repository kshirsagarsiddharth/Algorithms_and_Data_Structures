def lca_binary_tree(root,node1,node2):
    if root is None:
        return root
    if root is node1 or root is node2:
        return root
    left = lca_binary_tree(root.left,node1,node2)
    right = lca_binary_tree(root.right,node1,node2)

    if left is not None and right is not None:
        return root
    else:
        if left:
            return left
        else:
            return right

def lca_bst_iterative(root,node1,node2):
    while root:
        if root.data > node1 and root.data > node2:
            root = root.left
        elif root.data < node1 and root.data < node2:
            root = root.right
        else:
            break

        return root
