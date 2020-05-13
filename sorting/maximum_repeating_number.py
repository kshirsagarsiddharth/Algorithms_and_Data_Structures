"""
O(n),O(1)
"""

def max_repeating_element(array,size,max_range):
    for i in range(0,size):
        array[array[i] % max_range] += max_range

    maximum = array[0]
    result = 0
    for i in range(1,size):
        if array[i] > maximum:
            maximum = array[i]
            result = i
    return result

"""
O(nlogn),O(1)
"""
def most_frequent_elements(array,n):
    array.sort()
    max_count = 1
    res = array[0]
    current_count = 1

    for i in range(1,n):
        if array[i] == array[i - 1]:
            current_count += 1
        
        else:
            if current_count > max_count:
                max_count = current_count
                res = array[i - 1]
            
            current_count = 1

    if current_count > max_count:
        max_count = current_count
        res = array[n - 1]
    
    return res
arr = [1, 5, 2, 1, 3, 2, 1] 
n = len(arr) 
print(most_frequent_elements(arr, n)) 

"""
def most_frequent_elements(array,n):
	max_count = 1
	curr_count = 1
	array.sort()
	max_elem = array[0]

	for i in range(1,n):
		if array[i] == array[i - 1]:
			curr_count += 1
		else:
			if curr_count > max_count:
				max_count = curr_count
				max_elem = array[i - 1]
		
	if curr_count > max_count:
		max_count = curr_count
		max_elem = array[i - 1]
	
	return max_elem
		
"""

"""
O(n),O(n)
"""

def most_frequent(array,n):
    dictonary = {}
    for i in range(0,n):
        if array[i] in dictonary.keys():
            dictonary[array[i]] += 1
        else:
            dictonary[array[i]] = 1
    max_elem = max(dictonary.values())
    return [i for i in dictonary.keys() if dictonary[i] == max_elem][0]

