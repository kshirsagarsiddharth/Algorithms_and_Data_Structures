def local_minimum(array,n):

    low = 0
    high = n - 1

    while low <= high:

        mid = low + (high - low) // 2

        if (mid == 0 and array[mid + 1] > array[mid]) or (mid == n - 1 and array[mid - 1] > array[mid]) or (array[mid] < array[mid + 1] and array[mid] < array[mid - 1]):
            return array[mid]
        
        if mid > 0 and (array[mid] > array[mid - 1]):
            high = mid - 1
        else:
            low = mid + 1

arr = [4123, 3, 89, 14, 16, 40] 
n = len(arr) 

print(local_minimum(arr,n))