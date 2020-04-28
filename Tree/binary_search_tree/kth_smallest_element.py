count = 0
def k_th_smallest(root,k):
    global count
    if root is None:
        return root
    left  = k_th_smallest(root.left,k)
    if left:
        return left
    count += 1
    if count == k:
        return root
    return k_th_smallest(root.right,k)
