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

