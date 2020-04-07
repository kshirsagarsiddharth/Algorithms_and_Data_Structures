#
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    # we use two sets and add addresses of the nodes
    # if there are same addresses in the set then the sets are mergerd    
    def check_merge_using_hashing(self,list_one,list_two):
        set_one = set()
        set_two =set()
        current = list_one.head
        while(current.next):
            set_one.add(current)
            current = current.next
        current = list_two.head
        
        while(current.next):
            set_two.add(current)
            current = current.next
            
        if set_one.intersection(set_two):
            return True
        else:
            return False
    def check_merge_using_parallel_approach(self,list_one,list_two):
        curr_list_one = list_one
        curr_list_two = list_two
        len_list_one,len_list_two = 0,0
        current = curr_list_one.head
        while(current.next):
            len_list_one += 1
            current = current.next 
        current = curr_list_two.head
        while(current.next):
            len_list_two += 1
            current = current.next 
        curr_list_one = list_one
        curr_list_two = list_two
        curr_list_one = curr_list_one.head
        curr_list_two = curr_list_two.head
        if len_list_one > len_list_two:
            for i in range(len_list_one - len_list_two):
                curr_list_one = curr_list_one.next
        elif len_list_two > len_list_one:
            for i in range(len_list_two - len_list_one):
                curr_list_two = curr_list_two.next
        
        while curr_list_one != curr_list_two:
            curr_list_one = curr_list_one.next
            curr_list_two = curr_list_two.next
        return curr_list_one
            
    def check_merge_using_parallel_approach_num(self,list_1,list_2):
        # first we copy the two linked lists into two temp variables
        
        len_list_1,len_list_2 = 0,0 # creating two variables to store the list length 
        
        current = list_1.head
        while (current.next):
            len_list_1 += 1
            current = current.next
            
            
        current = list_2.head
        while (current.next):
            len_list_2 += 1
            current = current.next
        list_1 = list_1.head
        list_2 = list_2.head
        if len_list_1 > len_list_2:
            for i in range(len_list_1 - len_list_2):
                list_1 = list_1.next
        elif len_list_2 > len_list_1:
            for i in range(len_list_2 - len_list_1):
                list_2 = list_2.next
            
        while(list_1 != list_2):
            list_1 = list_1.next
            list_2 = list_2.next
        return list_1
            
        
        
    def insert_node_at_beginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def print_linked_list(self):
        temp = self.head
        while(temp):
            print(temp.data,end  = ' ')
            temp = temp.next

# code to check if above function works
ll1 = LinkedList()
array = [1,2,3,4,5,6,7]
for val in array:
    ll1.insert_node_at_beginning(val)

ll2 = LinkedList()
array = [10,9,8]
for val in array:
    ll2.insert_node_at_beginning(val)

  		

temp1 = ll1.head
for i in range(0,3):
    temp1 = temp1.next
temp2 = ll2.head

temp1.next = temp2
ll = LinkedList()
ll.check_merge_using_parallel_approach(ll1,ll2)       
                
    
    
            
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    