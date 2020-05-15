def search_circular_array(array,n,x):
    low,high =0, n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if x == array[mid]:
            return mid
        
        if array[mid] <= array[high]:
            if x > array[mid] and x <= array[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if array[low] <= x and x < array[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
    return -1