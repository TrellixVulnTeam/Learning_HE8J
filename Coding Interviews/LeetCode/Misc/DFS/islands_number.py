

grid = [
["1","1","0","0","0"],
  ["1","1","1","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","1","1"]
]


def numOfIslands(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    visited = set()
    count = 0
    for i in range(ROWS):
        for j in range(COLS):
                allPaths = []
                print(f"im at {i}, {j}")
                print(dfs(i,j,grid,visited, [], allPaths))
                print(allPaths)

    return count

def dfs(row, col, grid, visited, currentPath, allPaths):
    ROWS = len(grid)
    COLS = len(grid[0])

    size = 0
    #check rows/cols
    if row < 0 or row >= ROWS or col <0 or col >=COLS:
        return 0,[]
    if (grid[row][col] == str(0)):
        return 0,[]
    pos = str(row) + ',' + str(col)
    if pos in visited:
        return 0,[]
    visited.add(pos)

    size = 1
    currentPath = [pos]
    r = [-1, 0, 1]
    c = [-1, 0, 1]
    for rowDir in r:
        for colDir in c:
            dfs_size, dfs_path = dfs(row + r, col+ c, grid, visited, currentPath, allPaths)
            size += dfs_size
            dfs_path += dfs_path
   
    return size, currentPath

print(numOfIslands(grid))