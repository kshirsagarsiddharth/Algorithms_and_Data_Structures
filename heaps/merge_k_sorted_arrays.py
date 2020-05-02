class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists_brute_force(lists):
    nodes = []
    head = point = ListNode(0)
    for l in lists:
        while l:
            nodes.append(l.val)
            l = l.next
    for i in sorted(nodes):
        point.next = ListNode(i)
        point = point.next
    return head.next

"""
class LinkedNode:
    def __init__(self,data = 0,next = None):
        self.data = data
        self.next = next

def merge_k_sorted_linked_lists_brute_foce(lists):
    head = point = ListNode()
    nodes = []
    for List in lists:
        while List:
            nodes.append(List.data)
            List = List.next
    
    for i in sorted(nodes):
        point = ListNode(i)
        point = point.next

    return head.next

"""

from queue import PriorityQueue

def merge_k_lists_efficient(self,lists):
    head = point = ListNode()
    q = PriorityQueue()
    for List in lists:
        if List:
            q.put(List.data)
            List = List.next
    while not q.empty():
        point.next = ListNode(q.get())
        point = point.next
    return head.next

def merge_two_arrays(arr1,arr2,n1,n2):
    arr3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0
    
    while i < n1 and j < n1:

    #check if current element of the first array is smaller than the current element of the second array if yes store the first array element and increment first array index.

        if arr1[i] < arr2[j]:

            arr3[k] = arr1[i]
            i+= 1
            k+= 1
        
        else:
            arr3[k] = arr2[j]
            j+= 1
            k+= 1
    
    # store the remaning elements of the first aray

    while i < n1:
        arr3[k] = arr1[i]
        i+= 1
        k += 1
    
    while j < n2:
        arr3[k] = arr2[j]
        j+= 1
        k+= 1

    print('after merging the arrays are')
    for i in range(n1 + n2):
        print(arr3[i],end = " ")

"""
def merge_two_arrays(array1,array2,n1,n2):
    array3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0

    while i < n1 and j < n2:

        if array1[i] < array2[j]:
            array3[k] = array3[i]
            i+= 1
            k+= 1
        else:
            array3[k] = array2[j]
            j+= 1
            k+= 1
    
    while i < n1:
        array3[k] = array1[i]
        i+= 1
        k+= 1
    
    while j < n2:
        array3[k] = array2[j]
        j+= 1
        k+= 1
    print('the two merged arrays are')

    for i in range(n1 + n2):
        print(array3[i])
        

"""
    
def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists
            
    
