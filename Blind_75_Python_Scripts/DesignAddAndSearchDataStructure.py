class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.endOfWord = True


    def search(self,word):

        def dfs(index, root):
            cur = self.root

            for  i in range(index, len(word)):

                c = word[i]

                if c ==".":
                    for child in cur.children.values():
                        if dfs(i+1, child): # we're skipping the "."
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord

        return dfs(0, self.root)