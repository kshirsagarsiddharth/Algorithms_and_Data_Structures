import math
import sys
def merge_sort(array,start,end):
    if start < end:
        middle = math.floor((start + end) / 2) 

        merge_sort(array,start,middle)
        merge_sort(array,middle + 1,end)
        merge(array,start,middle,end)


def merge(array,start,middle,end):
    n1 = middle - start + 1
    n2 = end - middle
    left = [None] * (n1 + 1)
    right = [None] * (n2 + 1)
    for i in range(0,n1):
        left[i] = array[start + i]
    
    for j in range(0,n2):
        right[j] = array[middle + j + 1]

    left[n1] = sys.maxsize
    right[n2] = sys.maxsize

    i,j = 0,0
    for k in range(start,end + 1):
        if left[i] <= right[j]:
            array[k] = left[i] 
            i += 1
        else:
            array[k] = right[j]
            j += 1

data = [8, 7, 2, 1, 0, 9, 6]

merge_sort(data,start = 0,end = len(data) - 1)
print(data)

"""
import math
import sys

def merge_sort(array,start,end):
    middle = math.floor((start + end) / 2)
    merge_sort(array,start,middle)
    merge_sort(array,middle,end)
    merge(array,start,middle,end)

def merge(array,start,middle,end):
    n1 = middle - start + 1
    n2 = end - middle
    left = [None] * (n1 + 1)
    right = [None] * (n2 + 1)
    for i in range(0,n1):
        left[i] = array[start + i]

    for j in range(0,n2):
        right[j] = array[middle + j + 1]

    left[n1] = sys.maxsize
    right[n2] = sys.maxsize

    i,j = 0,0
    for k in range(start,end + 1):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

            

"""