import math as ma
def max_element_in_min_heap(heap):
    n = len(heap)
    max_element = ma.floor(n/2)
    for i in range(ma.floor(n/2) + 1,len(heap)):
        max_element = max(max_element,heap[i])
    return max_element
heap = [10, 25, 23, 45, 50, 30, 35, 63, 65, 81] 
