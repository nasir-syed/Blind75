class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right



def invert(root): # we have to swap the positions of the children
    if not root:
        return None

    tmp = root.left
    root.left = root.right
    root.right = tmp

    invert(root.left)
    invert(root.right)

    return root

