def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                (array[j],array[j + 1]) = (array[j + 1],array[j])

def bubble_sort_optmised(array):
    for i in range(len(array)):
        swapped = True
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                (array[j],array[j + 1]) = (array[j + 1],array[j])
                swapped = False
        
        if swapped == True:
            break
