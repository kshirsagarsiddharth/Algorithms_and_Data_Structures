import numpy as np
def insertion_sort(array):
    for step in range(len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key 


def ins_sort(array):
    for step in range(len(array)):
        key = array[step]
        j = step - 1

        while (j >=0 and array[j] > key):
            array[j + 1] = array[j]
            j = j - 1
            
        array[j + 1] = key

