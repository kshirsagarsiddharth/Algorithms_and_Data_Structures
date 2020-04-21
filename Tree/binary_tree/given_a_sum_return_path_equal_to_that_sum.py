class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def has_path_sum(root,sum2):
    if root is None:
        return sum2 == 0
    answer = 0
    sub_sum = sum2 - root.data
    if sub_sum == 0 and root.left is None and root.right is None:
        return True
    
    if root.left is not None:
        answer = answer or has_path_sum(root.left,sum2)
    
    if root.right is not None:
        answer = answer or has_path_sum(root.right,sum2)
    
    return answer

root = Node(10) 
root.left = Node(8) 
root.right = Node(2) 
root.left.right = Node(5) 
root.left.left = Node(3) 
root.right.left = Node(2)

print(has_path_sum(root,21))