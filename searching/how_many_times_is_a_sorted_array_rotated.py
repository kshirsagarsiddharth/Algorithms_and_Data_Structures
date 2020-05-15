# brute-force approach

def find_rotation_linear(array):
    minimum = array[0]
    minimum_index = 0
    for i in range(len(array)):
        if array[i] < minimum:
            minimum = array[i]
            minimum_index = i
    
    return minimum_index

# optimal approach

"""
case 1:
    array[low] <= array[high]:
        return low
    In this case the array is already sorted hence low is returned because index of low gives us the number of times the array is rotated

case 2:
    we have a very intreasting property for the pivot element, in the case of the pivot element the elements adjcent to this pivot are greater
    
    next = (mid + 1) % N
    previous = (mid + N - 1) % N

    array[mid] <= array[next] and array[mid] <= array[previous]
        return mid

case 3:
    In this case the whole segment is sorted hence the pivot element cannot exist in this (right) segment hence the (right) segment can be discarded.

    array[mid] <= array[high]
        high = mid - 1

case 4 : This case is same as the above case in this case the left segment is discarded.

    arrat[mid] >= array[low]
        low = mid + 1
"""

def find_rotation_counts(array,n):
    low,high = 0,n - 1

    while low <= high:

        if array[low] <= array[high]:
            return low

        mid = low + (high - low) // 2
        nxt = (mid + 1) % n
        prev = (mid + n - 1) % n

        if array[mid] <= array[nxt] and array[mid] <array[prev]:
            return mid

        elif array[mid] <= array[high]:
            high = mid - 1
        elif array[mid] >= array[low]:
            low = mid + 1

arr = [15, 18, 2, 3, 6, 12] 
n = len(arr)
print(find_rotation_counts(arr,n))