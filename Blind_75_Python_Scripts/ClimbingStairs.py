def climbStairs(n):
    one, two = 1, 1
    # dynamic programming involved
    for i in range(n-1):
        temp = one
        one = one+two
        two = temp

    return one



print(climbStairs(5))
# there are 8 ways to reach the fifth step