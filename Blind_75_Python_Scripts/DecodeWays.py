def decode(s):

    # "A" -> 1, "B" -> 2 ... "Z" -> 26

    dp = {len(s): 1}

    def dfs (i):

        if i in dp:
            return dp[i] # cached or end of the string
        if s[i] == "0":
            return 0 # we cant decode a 0, return 0 immediately

        res = dfs(i + 1)
        if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
            res += dfs(i+2)


        dp[i] = res

        return res

    return dfs(0)



s = "121"

print(decode(s))