def wordBreak(s, wordDict):
    dp = [False] * (len(s)+1)

    dp[len(s)] = True  # the last element is always set to true

    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i: i+len(w)] == w:
                # first we check if the length of the word is not out of bounds
                # and the word is present in the string from s[i : i+len(w)]

              dp[i] = dp[i + len(w)]

            if dp[i]:
                break # we dont need to go thru the other words since one has already matched

    return dp[0]

word = "leetcode"
wordDict = ["leet", "code"]

print(wordBreak(word,wordDict))