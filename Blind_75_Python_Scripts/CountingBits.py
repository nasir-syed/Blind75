def count(n):
    dp = [0] * (n+1) # 0 will always be there
    offset = 1

    for i in range(1, n+1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]

    return dp


print(count(2))

# 0 -> 0, it has no 1's in its binary representation
# 1 -> 1 has one 1 in its binary representation
# 2 -> 10 also has only one 1 in its binary representation
