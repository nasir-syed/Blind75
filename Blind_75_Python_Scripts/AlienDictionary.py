def alien(words):

    adj = {c: set() for w in words for c in w}
    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        minLen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""

        for j in range(minLen):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break

    visit = {} # false => visited, True => in the current path

    res =[]

    def dfs(c):

        # post order dfs

        if c in visit:
            return visit[c] # if its in visit, return their visit value (if false, then not been visited, else theres a loop)

        visit[c] = True

        for nei in adj[c]:
            if dfs(nei): # if there is aloop amon the neighbours, return true
                return True

        visit[c] = False
        res.append(c)


    for c in adj:
        if dfs(c): # if theres is a loop return
            return ""

    res.reverse()
    return "".join(res)


words = ["wrt", "wrf", "er", "ett","rftt"]

print(alien(words))