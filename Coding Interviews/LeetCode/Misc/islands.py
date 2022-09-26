
def dfs(grid, row, col, visited, allPaths, temporary_path):
        validRow = row < len(grid) and row >= 0
        validCol = col < len(grid[0]) and col >= 0
        if not validRow or not validCol: return 0

        if grid[row][col] == "0":
            return 0

        pos = str(row) +"," + str(col)
        if pos in visited:
            return 0
        visited.add(pos)


        temporary_path.append(pos)
       
        size = 1
        size += dfs(grid, row + 1, col, visited,allPaths, temporary_path)
        size += dfs(grid, row - 1, col, visited,allPaths, temporary_path)
        size += dfs(grid, row, col + 1, visited,allPaths, temporary_path)
        size += dfs(grid, row, col - 1, visited, allPaths, temporary_path)

        #means no more increase in size!
        if size == 1:
            allPaths.append(list(temporary_path))

        del temporary_path[-1]

        return size

def numIslands(grid) -> int:
        count = 0
        ans = []
        locations = []
       
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                allPaths = []
                size = dfs(grid, i,j, visited, allPaths, []) 
                if size != 0:
                    list(visited)
                    count += 1
                    ans.append(size)
                    print(allPaths)
        print(locations)
        print(ans)
        return count

grid = [
    ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid))