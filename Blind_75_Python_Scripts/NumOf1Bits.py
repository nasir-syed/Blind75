def check(input):

    # res = 0
    # while input:
    #     res += input % 2
    #     n = n >> 1
    # return res

    # the above is O(1) time complexity, goes thru all elements

    res = 0
    while input:
        input = input & (input - 1) # basically subtracting a 1 bit everytime
        res += 1

    return res

    # the above algorithm, goes thru all the 1's and takes less time



