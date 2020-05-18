def find_pivot(array,n):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] > array[mid + 1] and array[mid] > array[mid - 1]:
            return mid
        
        if array[mid] <= array[high]:
            high = mid - 1
        else: # array[]
            low = mid + 1
    return -1
def binary_search(array,n,x):
    low,high = 0,n - 1
    while low <= high:
        mid = low + ((high - low)) // 2
        if x == array[mid]:
            return mid
        elif x > array[mid]:
            low = mid + 1
        else:
            high = mid - 1

def pivoted_binary_search(array,n,x):
    pivot = find_pivot(array,n)

    if pivot == -1:
        return binary_search(array,n,x)
    
    if pivot == x:
        return pivot
    
    if array[0] <= x:
        return binary_search(array,0,pivot - 1,x)
    else:
        return binary_search(array,pivot + 1,n - 1,x)
        

