class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left


def max(root):
    # if the children are negative, we'll not include them

    res = [root.val]


    # return max path sum without splitting
    def dfs(root):
        if not root:
            return 0

        leftMax = max(dfs(root.left), 0)
        rightMax = max(dfs(root.right), 0)

        # compute max path sum WITH splitting
        res[0] = max(res[0], root.val + leftMax + rightMax)

        return root.val + max(leftMax, rightMax)

    dfs(root)
    return res[0]