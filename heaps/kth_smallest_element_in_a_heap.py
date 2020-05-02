import math
def heapify(array,array_len,i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < array_len  and array[i] > array[l]:
        smallest = l
    
    if r < array_len and array[smallest] > array[r]:
        smallest = r

    if smallest != i:
        array[i],array[smallest] = array[smallest],array[i]
        heapify(array,array_len,smallest)
    

def build_min_heap(array,len_array):
    for i in range(math.floor(len_array/2) - 1,-1,-1):
        heapify(array,len_array,i)

def kth_smallest(collection,k):
    """Return kth smallest element in a collection """
    A = collection[:k]
    build_min_heap(A)
    for i in range(0,len(collection)):
        if collection[i] < A[0]:
            A[0] = collection[i]
            heapify(A,0,k)
    return A[0]
    
