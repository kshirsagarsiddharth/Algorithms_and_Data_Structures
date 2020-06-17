from collections import deque

def level_order(root):
    if not root:
        return []
    queue = deque([root])
    result  =[]
    while queue:
        curr_level,size = [],len(queue)
        for _ in range(size):
            temp = queue.popleft()
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        
        curr_level.append(temp.left)
    result.append(curr_level)

    return result

"""
Level order Traversal recursive
"""

def level_order(root):
    res = []
    def dfs(root,level,res):
        if not root:
            return
        
        if len(res) < level + 1:
            res.append([])
        
        res[level].append(root.val)
        dfs(root.left,level + 1,res)
        dfs(root.right,level + 1,res)

    dfs(root,0,res)

    return res

