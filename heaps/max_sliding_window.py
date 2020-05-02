def max_sliding_inefficient(array,k):
    n = len(array)
    for i in range(n - k + 1):
        maximum = array[i]
        for j in range(1,k):
            if array[i + j] > maximum:
                maximum = array[i + j]
        print(maximum)

# python program to find the maximum for each and every contiguous subarray of size k
from collections import deque

def print_max_efficient(arr,n,k):
    """
    create a doubally ended queue qi that stores indexes of the array elements the queue will store the indexes of every useful elementy in every window and it will maintain a decreasing order value from front to rear in Qi 

    """
    Qi = deque()
    # process first k or the first window elements of the array
    for i in range(k):
        # for every element the previous smaller elements are useless so remove them from qi
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()

        Qi.append(i) # add new elements to the rear of the queue

    # process the rest of the elements i.e from arr[k] to arr[n - 1]
    for i in range(k,n):
        print(str(arr[Qi[0]]) + " ",end = " ")

        # remove the elements which are out of the window
        while Qi and Qi[0] <= i - k:

            # remove from fromt of the deque
            Qi.popleft()

        #remove all the elements smaller than the currently being added elements

        while Qi and arr[i] > arr[Qi[-1]]:
            Qi.pop()
        
        Qi.append(i)

    print(str(arr[Qi[0]]))

# PLEACE REFER THE CODE BELOW

"""
from collections import deque

def print_max_efficient(arr,n,k):
	Deque = deque()

	for i in range(k):
		if deque and arr[i] >= arr[Deque[-1]]:
			Deque.pop()
		Deque.append(i)

	for i in range(k,n):
		print(arr[Deque[0]])

		if Deque and Deque[0] <= i - k:
			Deque.popleft()

		if deque and arr[i] > arr[Deque[-1]]:
			Deque.pop()
		
		Deque.append(i)
	
	print(arr[Deque[0]])
"""