"""arr = [1, 30, 40, 50, 60, 70, 23, 20] 
n = len(arr) 
# brute force approach O(n)
for i in range(0,len(arr) - 1):
    if arr[i] > arr[i + 1]:
         print(arr[i])
         break
"""

def find_maximum_recursive(array,low,high):
    # only one element is present in the array
    if low == high:
        return array[low]

    # if there are two elements and first is greater than the second element than then the first element is maximum

    if high == low + 1 and array[low] >= array[high]:
        return array[low]
    
    if high == low + 1 and array[high] >= array[low]:
        return array[high]

    mid = (high + low) // 2

    # if we reach at the point where mid is greater than its adjcent elements than the mid element is maximum
    if array[mid] > array[mid + 1] and array[mid] > array[mid - 1]:
        return array[mid]
    
    if array[mid] > array[mid + 1] and array[mid] < array[mid - 1]:
        return find_maximum_recursive(array,low,mid - 1)
    else:
        return find_maximum_recursive(array,mid + 1,high)
    
def find_maximum_iteative(array,low,high):
    
    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] > array[mid + 1] and array[mid] > array[mid - 1]:
            return array[mid]

        if array[mid] > array[mid - 1] and array[mid] < array[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1

