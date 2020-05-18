# approach one
def find_count_one(A,n,x):
    count = 0
    for i in range(0,n):
        if A[i] == x:
            count += 1
    return count
# approach two
def find_count_two(A,n,x):
    count = 0
    for i in range(0,n):
        if A[i] == x:
            count += 1
        elif A[i] > x:
            break
    return count

# approach three
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

def find_count_three(array,n,x):
    first_occ = first_occurance(array,n,x)
    last_occ = last_occurance(array,n,x)

    return first_occ - last_occ + 1


def binary_search(array,n,x):
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

def count_occurance(array,n,x):
    index = binary_search(array,n,x)

    if index == -1:
        return False
    
    count = 1
    left = index - 1
    while left >= 0 and array[left] == x:
        count += 1
        left -= 1
    
    right = index + 1
    while right < n and array[right] == x:
        count += 1
        right += 1
    
    return count

