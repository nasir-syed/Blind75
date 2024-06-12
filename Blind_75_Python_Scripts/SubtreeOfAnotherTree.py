class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right





def isSubTree(s, t):
    if not t:
        return True # if the subtree is empty and the other is not, then it will always be a subtree


    # we dont have to include "and t" because the above would'vealready been executed by this point

    if not s:
        return False


    if sameTree(s,t):
        return True #if both are smae then they are a subtree of one another


    return isSubTree(s.left, t.left) or isSubTree(s.right, t.right) # we use or here, cuz if its is present in even one side then it is a subtree





def sameTree(s, t):
    if not s and not t:
        return True  # if both are null then a null subtree is a subtree of a null tree

    if s and t and s.val == t.val:
        return sameTree(s.left, t.left) and sameTree(s.right, t.right)

    return False # one tree is empty the other is not empty, so we return false, they are not the same tree
