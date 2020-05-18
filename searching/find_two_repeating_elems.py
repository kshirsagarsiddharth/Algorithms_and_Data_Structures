# %%

# Finding two repeating elements in an array

class Method_one:
    def find_repeating_elems(self,array,n):
        for i in range(0,n):
            for j in range(i + 1,n - 1):
                if array[i] == array[j]:
                    return True

m1 = Method_one()
array = [4, 2, 4, 5, 2, 3, 1] 
m1.find_repeating_elems(array,len(array))

# %%
class Method_two:
    def find_repeating(self,array,size):
        count = [0] * size
        for i in range(0,size):
            if count[array[i]] == 1:
                print(array[i])
            else:
                count[array[i]] += 1
m2 = Method_two()
m2.find_repeating(array,len(array))
 

# %%
import math
math.factorial(2)

# %%
import math
def find_repeating_elems(array,size):
    n = size - 2
    product = 1
    array_summation = sum(array)
    natural_summation = n * (n + 1) // 2
    for i in array:
        product *= i
    product = product / math.factorial(n)

    alpha = array_summation - natural_summation
    beta = math.sqrt(math.pow(alpha,2) - 4 * (product))

    X = (alpha + beta) // 2

    Y = (alpha - beta) // 2

    return (X,Y)