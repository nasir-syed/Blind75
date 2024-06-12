def topFreq(nums, k):
    count = {} #hashmap
    freq = [[] for i in range(len(nums)+1)]


    for n in nums:
        count[n] = 1 + count.get(n, 0) # 1 + current count of occurences (if null, then 0)
    for n, c in count.items:
        freq[c].append(n) #add the key value pairs to freq

    res = []

    for i in range(len(freq-1, 0, -1)): # iterating in reverse
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

