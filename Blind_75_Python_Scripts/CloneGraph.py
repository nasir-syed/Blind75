"""
# definition for a node
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

def cloneGraph(node):

    oldToNew = {} # creating a hashmap to store created copies


    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]

        copy = Node(node.val)
        oldToNew[node] = copy

        for neighbour in node.neighbors:
            copy.neighbors.append(dfs(neighbour)) # the neighbours of the node are also copied and added

        return copy

    return dfs(node)

