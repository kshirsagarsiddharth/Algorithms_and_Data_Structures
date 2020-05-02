def smallestRange(self, A):
        ans = -1e9, 1e9
        for right in sorted(set(x for l in A for x in l))[::-1]:
            for B in A:
                while B and right < B[-1]:
                    B.pop()
                if not B:
                    return ans
            left = min(B[-1] for B in A)
            if right - left <= ans[1] - ans[0]:
                ans = left, right
        return ans

arr = [ 
    [4, 7, 9, 12, 15], 
    [0, 8, 10, 14, 20], 
    [6, 12, 16, 30, 50] 
    ] 
