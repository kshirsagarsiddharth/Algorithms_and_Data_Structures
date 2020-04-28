class KaryTree:
    def __init__(self,data):
        self.data = data
        self.children = []

def build_k_ary_tree(array,k):
    n = len(array)
    if n <= 0:
        return None
    index = 0
    root = KaryTree(array[0])
    if root is None:
        return None
    queue = []
    queue.append(root)
    while len(queue) > 0:
        temp = queue.pop(0)
        for i in range(0,k):
            index += 1
            if index < n:
                temp.children.insert(i,KaryTree(array[index]))
                queue.append(temp.children[i])
    return root


def kary_tree(array,k):
    index = 0
    if array is None:
        return None
    queue = []
    root = KaryTree(array[0])
    if root is None:
        return None
    
    queue.append(root)

    while len(queue) > 0:
        temp = queue.pop(0)
        for i in range(0,k):
            index += 1
            temp.children.insert(i,array[index])
            queue.append(temp.children[i])
    
    return root

























