import collections


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

# recursive dfs
def maxDepth(root):
    if not root:
        return 0 # if tree empty

    return 1 + max(maxDepth(root.left), maxDepth(root.right))



# iterative bfs ( number of levels/layers == depth)
def bfsMaxDepth(root):
    if not root:
        return 0

    level = 1
    q = collections.deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft() # remove from the queue

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            level += 1

    return level


# iterative DFS
def dfsMaxDepth(root):
    
    stack = [[root, 1]]
    res = 0

    while stack:
        node, depth = stack.pop()

        if node:  #if node not null
            res = max(res, depth)
            stack.append([node.left, depth+1])
            stack.append([node.right, depth+1])


    return res
