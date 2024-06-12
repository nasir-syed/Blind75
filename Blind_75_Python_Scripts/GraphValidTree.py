def validTree(n, edges):
    if not n :
        return True # an empty graph counts as a tree

    adj = {i: [] for i in range(n)}

    for n1, n2 in edges:
        adj[n1].append[n2]
        adj[n2].append[n1]

    visit = set()
    def dfs(i , prev):
        if i in visit:
            return False

        visit.add(i)

        for nei in adj[i]:
            if nei == prev:
                continue
                # we don't want to vist the same node again,
                # so if it is a neighbour and the previous node we visited, we will simply not visit it

            if not dfs(nei, i): # i will be the previous node visited and the neighbour will be next
                return False # if we detect a loop among the neighbour's neighbours then we return false
        return True # we did not detect a loop anywhere



    return dfs(0, -1)  and n == len(visit)
    # we will set the first node's neighbour as -1, which will never exist in a graph as it alwayss starts from 0
    # and there are no nodes left unconnected in the tree
