def search(board, word):
    ROWS, COLS = len(board), len(board[0])

    path = set() # we can't use the same value, so we keep track of their position


    def dfs(r, c, i): # i -> current character of the word
        if i == len(word):
            return True # we reached the end of the word

        if (r < 0 or c < 0 or \
        r >= ROWS or c >= COLS or \
        word[i] != board[r][c] or \
        (r,c) in path):
            return False

        path.add(r,c) # currently searching, prevents going back to the previous element
        # or reusing the element

        # search the top, bottom, left and right of the position
        res = (dfs(r + 1, c, i + 1) or \
               dfs(r, c + 1, + i + 1) or \
                dfs(r - 1, c, + i + 1) or \
                 dfs(r, c - 1, + i + 1))

        path.remove((r,c)) # remove from path after its done
        return res


    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0): return True
        return False


