# finding iteratively number of childrens in a given tree
class Node:
    def __init__(self,data = None):
        self.data = data
        self.child = []

def number_of_children(root,value):
    # initializing the number of childrens as zero
    children = 0
    if root == None:
        return 0
    # create a queue and append the root
    queue = []
    queue.append(root)

    while len(queue) > 0:
        n = len(queue)

        # if this node has children

        while n > 0:
            # deque an item from the queue and check if it is 
            # equall to x if yes than return number of children
            temp = queue.pop(0)
            if temp.data == value:
                children = children + len(temp.child)
                return children
        
            # enque all the childrens of the dequed item0
            for i in range(0,len(temp.child)):
                queue.append(temp.child[i])
            n -= 1
    return children
            

root = Node(20) 
(root.child).append(Node(2)) 
(root.child).append(Node(34)) 
(root.child).append(Node(50)) 
(root.child).append(Node(60)) 
(root.child).append(Node(70)) 
(root.child[0].child).append(Node(15)) 
(root.child[0].child).append(Node(20)) 
(root.child[1].child).append(Node(30)) 
(root.child[2].child).append(Node(40)) 
(root.child[2].child).append(Node(100)) 
(root.child[2].child).append(Node(20)) 
(root.child[0].child[1].child).append(Node(25)) 
(root.child[0].child[1].child).append(Node(50)) 
number_of_children(root,50)


