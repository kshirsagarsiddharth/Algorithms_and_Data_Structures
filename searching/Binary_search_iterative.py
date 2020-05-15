def binary_search_iterative(array,n,x):
    """
        over here array is the input array n is the array length and x is the element to be searched
    """

    low,high = 0,n - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if x == array[mid]:
            return mid
        elif x > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
        
    return -1

array = [ 3, 4, 5, 6, 7, 8, 9 ] 
x = 4
print(binary_search_iterative(array,len(array),x))

def binary_search_recursive(array,low,high,x):
    
    if low > high:
        return -1
    mid = low + ((high - low) // 2)
    if array[mid] == x:
        return mid
    
    elif array[mid] > x:
        return binary_search_recursive(array,low,mid - 1,x)
    else:
        return binary_search_recursive(array,mid + 1,high,x)

print(binary_search_recursive(array,0,len(array) - 1,4))

