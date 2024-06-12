import collections


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right




def levelOrder(root):
    res = []

    q = collections.deque()
    q.append(root)

    while q:
        qLen = len(q)
        level = []

        for i in range(qLen):
            node = q.popleft()

            if node: # if node is not null
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)

        if level:
            res.append(level) # we are not adding null nodes to level list

    return res