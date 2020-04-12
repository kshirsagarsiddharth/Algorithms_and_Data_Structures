stack = [4, 5, -2, -3, 11, 10, 5, 6, 20,76]
def check_if_elements_consecutive(stack):
    auxilary_stack = []
    for val in stack:
        auxilary_stack.append(val)
    
    if len(auxilary_stack) % 2 == 1:
        print('the stack is odd')
        auxilary_stack.pop()
    
    for i in range(len(auxilary_stack) - 1):
        if len(auxilary_stack) == 0:
            break
        else:
            val1 = auxilary_stack.pop()
            val2 = auxilary_stack.pop()
            if abs(val1 - val2) == 1:
                print('good')
            else:
                 print(i)
                 return False
            
            if len(auxilary_stack) == 0:
                print('the elements are consecutive')


'''
auxilary_stack = []
for val in stack:
    auxilary_stack.append(val)

if len(auxilary_stack) % 2 == 1:
    print('the stack is odd')
    auxilary_stack.pop()

for i in range(len(auxilary_stack) - 1):
    if len(auxilary_stack) == 0:
        break
    else:
        val1 = auxilary_stack.pop()
        val2 = auxilary_stack.pop()
        if val1 == val2:
            print('good')
        else:
             False
        
        if len(auxilary_stack) == 0:
            print('the elements are consecutive')
'''

def pairwise_consecutive(stack):
    aux = []
    while(len(stack) != 0):
        aux.append(stack[-1])
        stack.pop()