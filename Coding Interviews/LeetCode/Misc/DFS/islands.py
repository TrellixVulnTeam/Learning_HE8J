grid = [
    ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


def numOfIslands(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    visited = set()
    count = 0
    for i in range(ROWS):
        for j in range(COLS):
                print(f"im at {i}, {j}")
                if dfs(i, j, grid, visited):
                    count += 1
    return count

def dfs(row, col, grid, visited):
    ROWS = len(grid)
    COLS = len(grid[0])
  
     #check rows/cols
    if row < 0 or row >= ROWS or col <0 or col >=COLS:
        return False
  
    if (grid[row][col] == str(0)):
        return False

    pos = str(row) + ',' + str(col)
    if pos in visited:
        return False
    visited.add(pos)

    dfs(row, col+1, grid, visited)
    dfs(row, col-1, grid, visited)
    dfs(row + 1, col, grid, visited)
    dfs(row - 1, col, grid, visited)

    return True

print(numOfIslands(grid))