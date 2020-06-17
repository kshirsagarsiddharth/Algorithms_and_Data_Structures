def inorder_traversal(root):
    ans = []
    def helper(root):
        if root:
            helper(root.left)
            ans.append(root.val)
            helper(root.right)
    
    helper(root)

    return ans
