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


def heap_sort(array):
    array_len = len(array)
    for i in range(math.floor(array_len/2)-1 ,-1,-1):
        heapify(array,array_len,i)

    for i in range(array_len - 1,0,-1):
        array[i],array[0] = array[0],array[i]

        heapify(array,i,0)

def heap_sort(array):
    # convert the array into max heap
    array_len = len(array)
    for i in range(math.floor(array_len /2) - 1,-1,-1):
        heapify(array,array_len,i)

    # heap sort the elements
    for i in range(len(array) - 1,0,-1):
        array[0],array[i] = array[i],array[0]
        heapify(array,i,0)  # this is done because we are excluding those values, which are already removed during the process and max heapify uis limited to the array eolements which are yet to be processed i.e genrally we are process ing the array length from the behind.


