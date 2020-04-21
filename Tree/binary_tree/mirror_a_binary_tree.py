class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def to_mirror_binary_rec(root):
    if root is None:
        return
    to_mirror_binary_rec(root.left)
    to_mirror_binary_rec(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp

"""
    perform iterative inorder traversal of one tree and iterative reverse inorder traversal of the 
    another tree in parallel

    During this corresponding iterative traversal check if the nodes have the same values or not
    if not same they are not mirrors of each other.

    If the values are same than check that at any point in the inorder traversal one of the root
    becomes null and the other is not null.
    if this happens than they are not mirrors of each other.
    if corresponding nodes in the two traversal have different data values then they are not mirrors

    if at any point one root becomes None and other is not none , then the trees are not mirroers.
    this condition verifies that structures of the tree are 
    miror of each other
"""

def are_mirrors_iterative(root_one,root_two):
    stack_one = []
    stack_two = []
    while True:
        while root_one is not None and root_two is not None:
            if root_one.data != root.data:
                return False
            stack_one.append(root_one)
            stack_two.append(root_two)
            root_one = root_one.left
            root_two = root_two.right
        if (root_one is None and root_two is not None) or (root_one is not None and root_two is None):
            return False

        if len(stack_one) != 0 and len(stack_two) != 0:
            root_one = stack_one.pop()
            root_two = stack_two.pop()

            # we have visited the nodes left subtree 
            # now the time is for right
            root_one = root_one.right

            root_two = root_two.left

        else:
            break
    return True

        
def are_mirrors_it(root_one,root_two):
    stack_one = []
    stack_two = []
    while True:
        while root_one is not None and root_two is not None:
            stack_one.append(root_one)
            stack_two.append(root_two)
            root_one = root_one.left
            root_two = root_two.right

        #if (not(root_one is None and root_two is None)):
           # return False
        if (root_one is None and root_two is not None) or (root_one is not None and root_two is None):
            return False

        if len(stack_one) != 0 and len(stack_two) != 0:
            root_one = stack_one.pop()
            root_two = stack_two.pop()
            root_one = root_one.right
            root_two = root_two.left

        else:
            break
    return True


def are_mirrors_recursive(root_one,root_two):
    if root_one is None and root_two is None:
        return True
    if root_one is None or root_two is None:
        return False
    if root_one.data != root_two.data:
        return False
    inorder = are_mirrors_recursive(root_one.left,root_two.right)
    rev_inorder = are_mirrors_recursive(root_one.right,root_two.left)

    return inorder and rev_inorder

        


root = Node(1)  
root.left = Node(2)  
root.right = Node(3)  
root.left.left = Node(4)  
root.left.right = Node(5) 

root1 = Node(1) 
root2 = Node(1) 
  
root1.left = Node(2) 
root1.right = Node(3) 
root1.left.left = Node(4) 
root1.left.right = Node(5) 
  
root2.left = Node(3) 
root2.right = Node(2) 
root2.right.left = Node(5) 
root2.right.right = Node(4) 

print(are_mirrors_recursive(root1,root2))
