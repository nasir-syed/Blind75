class TreeNode:
    def ___init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def serialize(root):
    # turns the tree into a string


    res = []

    def dfs(node):
        if not node:
            res.append("N") # if null we append N to symbolize it

            return

        res.append(node.val) # if not null the append the value
        dfs(node.left)
        dfs(node.right)

        # don't have to return any value here, changes are made to res directly


    dfs(root)
    return ",".join(res)


def deserialize(data):
    vals = data.split(",")
    global i
    i = 0

    def dfs():
        if vals[i] == "N":
            i += 1
            return None

        node = TreeNode(int(vals[i]))
        i += 1
        node.left = dfs()
        node.right = dfs()

        return node
    return dfs()