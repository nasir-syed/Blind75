def stock(prices):
    # after you sell there is a cooldown, you can't buy right after selling
    # can only keep one stock at a time, cant buy multiple at the same time
    # State: buying or selling?
    # Buying => i + 1
    # Selling => i + 2

    dp = {} # key = (i, buying) val = max_profit
    # the above is a hashmap

    def dfs(i, buying):
        if i >= len(prices):
            return 0 #if index exceeds length

        if(i , buying) in dp:
            return dp[(i, buying)] #if its is already stored in the hashmap, return it twin

        if buying:
            buy = dfs(i + 1, not buying) - price[i] # - price will be deducted to calculate how much profit we have
            cooldown = dfs(i + 1, buying) # skipping the current day
            dp[(i, buying)] = max(buy, cooldown)
        else:
            sell = dfs(i + 2, not buying) + price[i] # adding the price cuz we sold at that price, to get the profit
            cooldown = dfs(i + 1, buying) # skipping the current day
            dp[(i , buying)] = max(sell, cooldown)

        return dp[(i, buying)]

    return dfs(0, True)


prices = [1, 2, 3, 0, 1]
