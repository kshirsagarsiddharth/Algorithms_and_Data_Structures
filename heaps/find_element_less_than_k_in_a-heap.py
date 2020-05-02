def left(integer):
    return 2 * integer + 1

def right(integer):
    return 2 * integer + 2

def find_vals_less_than_k(heap,val,pos,len_heap):
    if val <= heap[pos]:
        return
    
    if pos > len_heap:
        return
    
    print(heap[pos])

    find_vals_less_than_k(heap,val,left(pos),len_heap)
    find_vals_less_than_k(heap,val,right(pos),len_heap)

heap = [1,2,3,4,5,6,7,8,9] 
val = 5
pos = 0
len_heap = len(heap)

find_vals_less_than_k(heap,val,pos,len_heap)
    
