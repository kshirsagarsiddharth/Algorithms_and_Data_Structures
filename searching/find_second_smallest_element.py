import sys
def find_second_smallest(array,n):
    first,second = sys.maxsize,sys.maxsize

    for i in range(0,len(array)):
        if array[i] < first:
            second = first
            first = array[i]
        elif array[i] < second and array[i] != first:
            second = array[i]
        
    if second == sys.maxsize:
        print("There is no second largest element")
    else:
        print(second , first)
arr = [12, 13, 1, 10, 34, 1]
print(find_second_smallest(arr,len(arr))) 