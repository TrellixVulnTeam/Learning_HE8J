
def solveSudoku(board) -> None:
    solve(board,0 ,0)


def isValid(row, col, grid ,k):
    k = str(k)
    validRow = k not in grid[row]
    validCol = k not in [grid[i][col] for i in range (0,9)]
    validSubGrid = k not in[grid[i][j] for i in range(row//3 * 3, row//3*3 + 3) for j in range (col//3*3, col//3*3 + 3)]
    return validRow and validCol and validSubGrid

def solve(grid, row, col):
    N = len(grid[0])
    if col == N:
        if row == N-1:
            return True
        else:
            col = 0
            row += 1

    if grid[row][col] != ".":
        return solve(grid, row, col+1)

    for i in range(1, 10):
        if isValid(row, col, grid, i):
            grid[row][col] = str(i)
            if (solve(grid, row, col+1)):
                return True
            grid[row][col] = "."
    
    return False







board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solveSudoku(board)

print(board)