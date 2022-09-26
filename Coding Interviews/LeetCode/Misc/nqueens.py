def nqueens(n):
    board = [["."] * n for i in range(n)]
    cols = set() 
    posDiag = set() # r + c
    negDiag = set() # r-c

    result = []
    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return

        for c in range(n):
            if c not in cols and r-c not in negDiag and r+c not in posDiag:
                board[r][c] = "Q"
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                backtrack(r + 1)

                board[r][c] ="."
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
        
        
    backtrack(0)
    return result

print(nqueens(4))