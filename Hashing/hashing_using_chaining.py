class ListNode:
    def __init__(self,key,val):
        self.pair = (key,val)
        self.next = None

class MyHashMap:
    def __init__(self):
        self.m = 1000
        self.h = [None] * self.m
    
    def put(self,key,val):
        index = key % self.m
        if self.h[index] == None:
            self.h[index] = ListNode(key,val)
        else:
            curr = self.h[index]
            while True:
                if curr.pair[0] == key:
                    curr.pair = (key,val)
                    return
                if not curr.next:
                    break
                curr = curr.next 
            curr.next = ListNode(key,val)

    def get(self,key):
        index = key % self.m
        curr = self.h[index]
        while curr:
            if curr.pair[0] == key:
                return curr.pair[1]
            else:
                curr = curr.next 
        return -1
    
    def remove(self,key):
        index = key % self.m
        curr = prev = self.h[index]
        if not curr:
            return
        if curr.pair[0] == key:
            self.h[index] = curr.next
        else:
            curr = curr.next 
            while curr:
                if curr.pair[0] == key:
                    prev.next = curr.next
                    break
                else:
                    curr,prev = curr.next,prev.next 
 
                


