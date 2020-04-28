class Node:
    def __init__(self,data = None):
        self.data = data
        self.child = []
def number_of_siblings(root,value):
    if root is None:
        return None
    queue = []
    queue.append(root)

    while len(queue) > 0:
        n = len(queue)
        while n > 0:
            temp = queue.pop(0)
            for i in range(0,len(temp.child)):
                if temp.child[i].data == value:
                    return len(temp.child) - 1
            
            for i in range(0,len(temp.child)):
                queue.append(temp.child[i])
            n -= 1

root = Node(50)  
(root.child).append(Node(2))  
(root.child).append(Node(30))  
(root.child).append(Node(14))  
(root.child).append(Node(60))  
(root.child[0].child).append(Node(15))  
(root.child[0].child).append(Node(25))  
(root.child[0].child[1].child).append(Node(70))  
(root.child[0].child[1].child).append(Node(100))  
(root.child[1].child).append(Node(6))  
(root.child[1].child).append(Node(1))  
(root.child[2].child).append(Node(7))  
(root.child[2].child[0].child).append(Node(17))  
(root.child[2].child[0].child).append(Node(99))  
(root.child[2].child[0].child).append(Node(27))  
(root.child[3].child).append(Node(16))  
print(number_of_siblings(root,100))
 

        
