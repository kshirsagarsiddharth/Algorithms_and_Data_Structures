# python program for radix sort
"""
in case of adix sort we apply count sort on each element in the array starting
from least significant bit to most significant bit
"""
# lets define the function radix sort
def countint_sort(array,place):
    size = len(array)
    count = [0] * 255
    output = [0] * size

    for i in range(0,size):
        index = array[i] // place
        count[index % 10] += 1
    
    for i in range(1,25):
        count[i] += count[i - 1]
    
    for i in range(size - 1,-1,-1):
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1

    for i in range(0,size):
        array[i] = output[i]

def  radix_sort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countint_sort(array,place)
        place *= 10

arr = [ 170, 45, 75, 90, 802, 24, 2, 66] 

radix_sort(arr)
print(arr)