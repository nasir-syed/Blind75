def replace(s, k):

    count = {} #hashmap to count the result of each char

    res, l = 0, 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0) # add 1 to the current value
        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1 # we shift the left pointer one place to the right
            # and so the value that was at the left pointer, will be removed

            l += 1

        res = max(res, r - l + 1) # r - l + 1 will give size of the window
    return res