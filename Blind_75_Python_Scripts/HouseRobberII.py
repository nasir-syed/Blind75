def rob(houses):


    def helper(houses):

        rob1, rob2 = 0, 0

        for n in houses:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2


    return max(houses[0], helper(houses[:-1]), helper(houses[1:]))



# the last and first houses are connected, kinda like a circle
houses = [2, 3, 2]
print(rob(houses))