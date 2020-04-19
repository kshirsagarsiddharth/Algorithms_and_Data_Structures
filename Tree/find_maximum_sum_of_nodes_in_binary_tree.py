class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def find_max_sum(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    height = 0
    max_sum = 0
    sum_array = []
    while len(queue) > 0:
        sum2 = 0
        node_count = len(queue)
        print(height)
        height += 1

        while (node_count > 0):
            temp = queue.pop(0)
            sum2 += temp.data
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
            node_count -= 1
        if sum2 > max_sum:
            max_sum = sum2
        sum_array.append([height,sum2])
    return sum_array

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left  = Node(4) 
root.left.right = Node(5) 
root.right.right = Node(8) 
root.right.right.left  = Node(6) 
root.right.right.right  = Node(7) 


import pandas as pd
df = pd.DataFrame(find_max_sum(root))
df[df[1] == max(df[1])][0]
 


