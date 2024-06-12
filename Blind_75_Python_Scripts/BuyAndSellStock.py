# buy low, sell high


def maxProfit (prices):
    l , r = 0, 1   # set a left and right pointer,
    # left pointer keeps track of lowest value we can buy, and
    # right pointer the highest we can sell for

    maxP = 0  # max profit

    while r < len(prices): # the right pointer keeps going till end of list
        if (l < r): # if sale (r) value is higher than buy (l) value

            prof = prices[l] - prices[r]
            maxP = max(maxP, prof)
        else:
            l = r # if not, move l to r position and increment r by 1
        r += 1

    return maxP



print(maxProfit([17,3,6,9,15,8,6,1,10]))