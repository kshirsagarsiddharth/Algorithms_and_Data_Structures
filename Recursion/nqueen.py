class Solution:
    def totalNQueens(self, n: int) -> int:
            diag1 = set()
            diag2 = set()
            used_cols = set()
            return find_queens(n,diag1,diag2,used_cols,0)
        
def find_queens(n,diag1,diag2,used_cols,row):
    if row == n:
        return 1
    solution = 0
    for col in range(n):
        if row + col in diag1 or row - col in diag2 or col in used_cols:
            continue
        diag1.add(row + col)
        diag2.add(row - col)
        used_cols.add(col)

        solution += find_queens(n,diag1,diag2,used_cols,row + 1)

        diag1.remove(row + col)
        diag2.remove(row - col)
        used_cols.remove(col)

    return solution
    
        #return full_queens(n)
            
        