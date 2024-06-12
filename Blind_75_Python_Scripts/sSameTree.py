class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right



def isSameTree(p, q):
    if not p and not q:
        return True # the trees are empty, so they are the same

    if not p or not q or p.val != q.val: # if either one is empty, or the values are not the same
        return False # if one is null and the other is not the they aren't the same tree


    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right) # both the left and right should return true for it to be the same 



