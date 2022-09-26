def wordsearch(board, word):
    ROWS = len(board)
    COLUMNS = len(board[0])
    path = set()

    #row, column, and index of word
    def dfs(r, c, i):
        if i == len(word):
            return True

        if r < 0 or c < 0 or r >= ROWS or c >= COLUMNS or board[r][c] != word[i] or (r,c) in path:
            return False
        
        path.add((r,c))
        res = dfs(r, c + 1, i+1) or dfs(r, c - 1, i+1) or dfs(r + 1, c, i+1) or dfs(r - 1, c, i+1)
        if res == True:
            return True
            
        path.remove((r,c))

        return res
    
    for i in range(ROWS):
        for j in range(COLUMNS):
            if dfs(i, j, 0):
                return True
        
    return False