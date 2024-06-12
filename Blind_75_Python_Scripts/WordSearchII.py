class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children
        cur.isWord = True # mark the end of the word



def findWords(board, words):
    root = TrieNode()
    for w in words:
        root.addWord(w)

    ROWS, COLS = len(board), len(board[0])
    res, visit = set(), set()

    def dfs(r, c, node, word):
        if (r < 0 or c < 0 or  # we go out of bounds
            r == ROWS or c == COLS # once again, out of bounds
            or (r,c) in visit or # already visited
            borad[r][c] not in node.children): # letter not it children, so word doesn't exists
            return

        visit.add(r,c)
        node = node.children(board[r][c])
        word += board[r][c] # add char to the word

        if node.isWord:
            res.add(word) # if the word is in the list of words, add to res

        dfs(r-1, c, node, word)
        dfs(r+1, c, node, word)
        dfs(r, c-1, node, word)
        dfs(r, c+1, node, word)
        visit.remove((r,c)) # after itself and its neighbours have been visited remove

    for r in range(ROWS):
        for c in range(COLS):
            dfs(r,c,root,"")


    return list(res) # convert to list to remove duplicates