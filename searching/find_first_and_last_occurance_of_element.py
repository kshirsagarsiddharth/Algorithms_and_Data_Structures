def first_occurance(array,n,x):
    low = 0
    high = n - 1
    result = -1
    while low <= high:
        mid = low + (high - low) // 2

        if x == array[mid]:
            result = mid
            high = mid - 1

        elif x < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return result

def last_occurance(array,n,x):
    low = 0
    high = n - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2

        if x == array[mid]:
            result = mid
            low = mid + 1

        elif x < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return result

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
n = len(arr) 
  
x = 8
print(first_occurance(arr,n,x))
print(last_occurance(arr,n,x))