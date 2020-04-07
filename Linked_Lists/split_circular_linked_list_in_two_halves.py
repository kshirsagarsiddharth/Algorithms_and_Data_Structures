# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:32:56 2020

@author: siddharth
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node
    
    def print_linked_list(self):
        if self.head is None:
            print('The linked list is empty')
        else:
            current = self.head
            print(current.data)
            current = current.next
            while(current.next is not self.head):
                print(current.data)
                current = current.next
                
    def print_linked_list_small(self):
        if self.head is None:
            print('The linked list doesnot exist')
        else:
            current = self.head
            while(current.next is not self.head):
                print(current.data)
                current = current.next
                
    def split_circular_linked_list(self,list1,list2):
       slow = self.head
       fast = self.head
       if self.head is None:
           return 
       while(fast.next is not self.head and fast.next.next is not self.head):
           fast = fast.next.next
           slow = slow.next
           
       if fast.next.next is self.head:
           fast = fast.next
       list1.head = self.head    
       if self.head.next is not self.head:
           list2.head = slow.next
           
       fast.next = slow.next
       
       slow.next = self.head
       
list_main = CircularLinkedList()
list1 = CircularLinkedList()
list2 = CircularLinkedList()

arr = [0,1,2,3,4,5,6,7,8,9,10]
for i in arr:
   list_main.insert_at_beginning(i)
    
list_main.split_circular_linked_list(list1, list2)         
            
                
                
                    
            
    