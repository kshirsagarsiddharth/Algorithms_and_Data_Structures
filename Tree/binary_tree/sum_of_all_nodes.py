class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def sum_of_all_nodes_recursive(root):
    if root is None:
        return 0
    left = sum_of_all_nodes_recursive(root.left) 
    right = sum_of_all_nodes_recursive(root.right)
    return root.data + left + right
sum2 = 0
def sum_of_all_nodes_iterative(root):
    global sum2
    if root is None:
        return -1
    queue = []
    queue.append(root)
    while len(queue) > 0:
        temp = queue.pop(0)
        sum2 += temp.data 

        if temp.left is not None:
            queue.append(temp.left)
        
        if temp.right is not None:
            queue.append(temp.right)
    return sum2

root = Node(1)  
root.left = Node(2)  
root.right = Node(3)  
root.left.left = Node(4)  
root.left.right = Node(5)  
root.right.left = Node(6)  
root.right.right = Node(7)  
root.right.left.right = Node(8)  
sum_of_all_nodes_recursive(root)

