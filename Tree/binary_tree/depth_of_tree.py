class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def max_depth(node):
    if node is None:
        return 0
    else:
        l_depth = max_depth(node.left)
        r_depth = max_depth(node.right)
        if l_depth > r_depth:
            return l_depth + 1
        else:
            return r_depth + 1
def iterative_tree_height(root):
    if root is None:
        return 
    queue = []
    queue.append(root)
    height = 0
    while True:
        node_count = len(queue)
        if node_count == 0:
            return height
        height += 1

        while (node_count > 0):
            temp = queue.pop(0)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
            
            node_count -= 1

root = Node(1) 
root.left = Node(2) 
root.left.right = Node(4)
root.right = Node(3)
root.right.right = Node(6)
root.right.right.left = Node(10)
max_depth(root)