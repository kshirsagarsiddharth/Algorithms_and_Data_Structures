def find_index_of_first_one(array,n):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2

        if array[mid] ==  1 and (array[mid - 1] == 0 or mid == 0):
            return mid
        
        if array[mid] == 1 :
            high = mid - 1
        else: # array[mid] == 0
            low = mid + 1

