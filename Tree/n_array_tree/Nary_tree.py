class TreeNode:
    def __init__(self,value,children = []):
        self.value = value
        self.childern = children

def size(root):
    count = 1
    for child in root.children:
        count += size(child)
    return count

def height(root):
    h = -1
    for child in root.children:
        h = max(h,height(child))
    return h + 1

def list_to_tree(array):
    if array == []:
        return []
    else:
        return TreeNode(array[0],[list_to_tree(value) for value in array[1:]])

def tree_to_list(root):
    return [root.value] + [tree_to_list(value) for value in root.children]

def contains(root,value):
    return root.value == value or any(contains(val,value) for val in root.children)

def find(root,value):
    if root.value == value:
        return root
    else:
        for val in root.children:
            answer = find(val,value)
            if answer != None:
                return answer
        return None

def ancestor(root,value):
    if root.value == value:
        return [value]
    else:
        for val in root.children:
            answer = ancestor(val,value)
            if answer != []:
                return [root.value] + answer
        return []