
class Node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None
head = None
prev = None
def convert(root,head):
    if root is None:
        return 
    global prev
    convert(root.left,head)
    if prev == None:
        head = root
    else:
        root.left = prev
        prev.right = root
    prev = root
    convert(root.right,head)

