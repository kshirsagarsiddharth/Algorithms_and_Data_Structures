import math
def heapify(array,array_len,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < array_len  and array[i] < array[l]:
        largest = l
    
    if r < array_len and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i],array[largest] = array[largest],array[i]
        heapify(array,array_len,largest)
    

def build_max_heap(array,len_array):
    for i in range(math.floor(len_array/2) - 1,-1,-1):
        heapify(array,len_array,i)

def merge_two_heaps(merged_array,array_n,array_m,array_n_len,array_m_len):
    for i in range(0,array_n_len):
        merged_array[i] = array_n[i]

    for i in range(0,array_m_len):
        merged_array[array_n_len + i] = array_m[i] 

    build_max_heap(merged_array,array_m_len + array_n_len)


"""def merge_two_heaps(merged_array,array_n,array_m,array_n_len,array_m_len):
    for i in range(0,array_n_len):
        merged_array[i] = array_n[i]
    
    for i in range(0,array_m_len):
        merged_array[n + i] = array_m[i]"""
