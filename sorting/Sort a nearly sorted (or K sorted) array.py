import heapq
def k_sorted_arrays(array,k):
    size = len(array)
    heap = array[0:k + 1]
    heapq.heapify(heap)
    index = 0
    for i in range(k + 1,size):
        array[index] = heapq.heappop(heap)
        heapq.heappush(heap,i)
        index += 1
    while heap:
        array[index] = heapq.heappop(heap)
        index += 1
    
    return array

k = 3
arr = [2, 6, 3, 12, 56, 8] 
print(k_sorted_arrays(arr,k))

