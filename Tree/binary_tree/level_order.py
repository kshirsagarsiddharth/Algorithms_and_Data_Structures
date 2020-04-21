class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def print_level_order(root):
    if root is None:
        return
    queue = []
    queue.append(root)

    while len(queue) > 0:
        print(queue[0].data)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

