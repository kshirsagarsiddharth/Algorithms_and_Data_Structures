n_a = -1
NA = -1
def move_to_end(m_plus_n,size):
    j = size - 1
    for i in range(size - 1,-1,-1):
        if m_plus_n[i] != n_a:
            m_plus_n[j] = m_plus_n[i]
            j -= 1
   
# merge array N of size n into array of  m_plus_n of size m + n

def merge(m_plus_n,N,m,n):
    i = n # current index of input part of m_plus_n
    j = 0 # current index of N
    k = 0 # current index of output m_plus_n

    while k < m + n:
        """
        Take an element from m_plus_n if 
            a -- value of the picked element is smaller and we have not reached at the end of it
            b -- we have reached the end of N[]
        """

        if (i < (m + n) and m_plus_n[i] <= N[j]) or (j == n):
            m_plus_n[k] = m_plus_n[i]
            k += 1
            i += 1
        else: # otherwise take the element form N[]

            m_plus_n[k] = N[j]
            k += 1
            j += 1

mPlusN = [2, 8, NA, NA, NA, 13, NA, 15, 20] 
N = [5, 7, 9, 25] 
n = len(N) 

m = len(mPlusN) - n 

