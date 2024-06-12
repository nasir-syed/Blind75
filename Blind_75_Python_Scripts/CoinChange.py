def coinChange(coins, amount):
    # how to get the target, in the LEAST amount of coins

    dp = [amount + 1] * (amount + 1)
    dp[0] = 0 # to get 0 you need 0 coins

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c]) #recurrence relation

    print(dp)

    return dp[amount] if dp[amount] != amount + 1 else -1

print(coinChange([1,3,4,5], 7))