import math
def heapify(array,array_len,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < array_len and array[i] < array[l]:
        largest = l
    if r < array_len and array[largest] < array[r]:
        largest = r
    
    if largest != i :
        array[i],array[largest] = array[largest],array[i]
        heapify(array,array_len,largest)  

def insert(array,new_val):
    array_len = len(array)
    if array_len == 0:
        array.append(new_val)
    else:
        array.append(new_val)
        for i in range(math.floor(array_len/2)-1 ,-1,-1):
            heapify(array,array_len,i)                      


def delete_node(array,num):
    array_len = len(array)
    for i in range(0,array_len):
        if num == array[i]:
            break
    array[i],array[array_len - 1] = array[array_len - 1],array[i]
    array.remove(array_len - 1)

    for i in range(math.floor(len(array)/2)-1 ,-1,-1):
            heapify(array,len(array),i) 

"""def delete_node(array,number):
    array_len = len(array)
    for i in range(0,array_len):
        if number == array[i]:
            break
    array[i],array[array_len - 1] = array[array_len - 1],array[i]
    array.remove(array_len - 1)

    for i in range(math.floor(len(array)/2 - 1),-1,-1):
        heapify(array,len(array),i)"""

arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)


