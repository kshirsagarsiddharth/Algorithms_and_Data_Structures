# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 00:15:51 2020

@author: siddharth
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_from_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_linked_list(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
    def merge_two_sorted_ll(self,list_1,list_2):
        

        while list_1 and list_2:
            if list_1.data <= list_2.data:
                temp = Node(list_1.data)
                list_1 = list_1.next
            else:
                temp = Node(list_2.data)
                list_2 = list_2.next
            temp = temp.next
        return temp
 
    
 
def merge_two_sorted_ll(list_1,list_2):
    ll = LinkedList()
    list_1 = list_1.head
    list_2 = list_2.head
    while list_1 and list_2:
        
        if list_1.data <= list_2.data:
            temp = Node(list_1.data)
            list_1 = list_1.next
        else:
            temp = Node(list_2.data)
            list_2 = list_2.next
        ll.insert_from_beginning(temp.data)
        temp = temp.next
        
    ll.print_linked_list()

def print_linked_list(ll):
        temp = ll.head
        while (temp):
            print(temp.data)
            temp = temp.next
ll1 = LinkedList()
for i in reversed(range(0,10,1)):
    ll1.insert_from_beginning(i)

ll2 = LinkedList()
for i in reversed(range(0,20,4)):
    ll2.insert_from_beginning(i)
merge_two_sorted_ll(ll1,ll2)
    
