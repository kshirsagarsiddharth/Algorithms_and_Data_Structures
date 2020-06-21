def isValidSudoku(board: List[List[str]]) -> bool:
    Set = set()
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j] != ".":
                val = board[i][j]

                if (i,val) in Set or (val,j) in Set or (i // 3,j // 3,val) in Set:
                    return False
                
                Set.add((i,val))
                Set.add((val,j))
                Set.add((i // 3, j // 3,val))
    return True