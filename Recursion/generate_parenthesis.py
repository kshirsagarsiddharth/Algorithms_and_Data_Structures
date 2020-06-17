ans = []
def generate(n,S = "",left = 0,right = 0):
    if len(S) == 2 * n:
        ans.append(s)
        return
    
    if left < n:
        generate(n,S + "(",left + 1,right)
    
    if right < left:
        generate(n,S + ")",left,right + 1)

"print answer in the terminal to check the result"
