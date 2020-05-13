def partition(array,start,end):
    pivot = array[end]
    i = start - 1
    # put the elements smaller than pivot on the left and elements large on the left 
    for j in range(start,end):
        if array[j] <= pivot:
            i += 1
            (array[i],array[j]) = (array[j],array[i])
    
    (array[i + 1],array[end]) = (array[end],array[i + 1])

    return i + 1

def quick_sort(array,start,end):
    if start < end:
        pi = partition(array,start,end)
        quick_sort(array,start,pi - 1)
        quick_sort(array,pi + 1,end)
    
array = [0,0,0,0,2,1,2,1,2,1,2,1,2,1,2,1,0,2,1,0,2,1,0,2,1]
quick_sort(array,0,len(array) - 1)

"""def partition(array,start,end):
    pivot = array[end]
    i = start - 1
    for j in range(start,end):
        if array[j] < pivot:
            i += 1
            (array[i],array[j]) = (array[j],array[i])
    (array[i + 1],array[end]) = (array[end],array[i + 1])

    return i + 1

def quick_sort(array,start,end):
    if start < end:
        pi = partition(array,start,end)
        quick_sort(array,start,pi - 1)
        quick_sort(array,pi + 1,end) 
"""