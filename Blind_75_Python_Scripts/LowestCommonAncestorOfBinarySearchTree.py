class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left





def lowestCommonAncestor(root, p, q):

    cur = root

    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right # if both elemnts are smaller, then its on the left side

        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left# if both elements are bigger then its on the right side

        else: # if a split occurs, or found one of the values p or q
            return cur

