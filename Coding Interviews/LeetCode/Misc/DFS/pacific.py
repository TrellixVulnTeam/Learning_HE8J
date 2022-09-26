
def pacificAtlantic(heights):
    ROWS = len(heights)
    COLS = len(heights[0])
    pacific = set()
    atlantic = set()
    
    def dfs(r,c,visited,prevHeight):
      
        if r < 0 or c<0 or r>= ROWS or c >= COLS or heights[r][c] < prevHeight or (r,c) in visited:
            return
        
    

        height = heights[r][c]
        visited.add((r,c))
    
 
        dfs(r, c+1, visited, height)
        dfs(r, c-1, visited, height)
        dfs(r+1, c, visited, height)
        dfs(r-1, c, visited, height)

        return
    
    #first and last row
    for c in range(COLS):
        dfs(0, c, pacific, heights[0][c])
        dfs(ROWS-1 , c, atlantic,heights[ROWS-1][c])
    
    #first and last col
    for r in range(ROWS):
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, COLS -1,atlantic, heights[r][COLS-1])
    ans =[]
    for i in range(ROWS):
        for j in range(COLS):
            if (i,j) in pacific and (i,j) in atlantic:
                ans.append((i,j))  
    print(len(atlantic))
    print(len(pacific))
    print(len(ans))
    return ans

board =[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
pacificAtlantic(board)