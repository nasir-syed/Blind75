class TrieNode:
    def __init__(self):
        self.children = {} # hashmap
        self.endOfWord = False

class Trie:
    def __init(self):
        self.root = TrieNode() # create a empty root TrieNode

    def insert(self,word):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode() 
                # if the letter doesn't exist in the tree, create a node for it
                # if it already existed, we would move to it instead making a new one 
            cur = cur.children[c]
        cur.endOfWord = True # mark the end of the word            

    def search(self,word):
        cur = self.root
        
        
        for c in word:
            if c not in cur.children:
                return False # not in the tree
            cur = cur.children[c]
        return cur.endOfWord

            
    
    def startsWith(self,prefix):
        cur = self.root


        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
    