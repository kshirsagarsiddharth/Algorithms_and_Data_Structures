import time 
import itertools as it 
def is_soluution_bruteforce(perm):
    for (i1,i2) in it.combinations(range(len(perm)),2):
        if abs(i1 -i2) == abs(perm[i1] - perm[i2]):
            return False 
    return True 

for perm in it.permutations(range(8)):
    if is_soluution(perm):
        print(perm)



def generate_permutations(perm, n):
    """
    perm: permutation array
    n: number of elements for generation of permution

    returns: prints number of permutations for a given number
    """
    if len(perm) == n:
        print(perm)
        return 
    
    for k in range(n):
        if k not in perm:
            perm.append(k)
            generate_permutations(perm, n)
            perm.pop()

generate_permutations(perm = [], n = 7)

def can_be_extended(perm):
    """
    This function checks wether wrt a given queen can it fit considering previous queens
    """
    i = len(perm) - 1 
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False 
    
    return True 

def extend(perm,n):
    """
    This function finds all the queens wrt back tracking
    """

    if len(perm) == n:
        print(perm)
        exit()
    
    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_be_extended(perm):
                extend(perm,n)
            
            perm.pop()
