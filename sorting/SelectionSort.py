def selection_sort(array,size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1,size):
            if array[i] < array[min_idx]:
                min_idx = i
        
        (array[step],array[min_idx]) = (array[min_idx],array[step])


def selec_sort(array,size):
    for step in range(len(array)):
        min_idx = step

        for i in range(step + 1,size):
            if array[i] < array[min_idx]:
                min_idx = i

        (array[step],array[min_idx]) = (array[min_idx],array[step])