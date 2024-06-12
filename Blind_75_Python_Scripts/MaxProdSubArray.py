def maxProd(nums):
    # we are going to be keeping track of minimum as well
    # if the element is 0, we are going to rest the max and min

    result = max(nums) # we're gonna set it to the largest element, rather than 0

    curMax, curMin = 1, 1

    for n in nums:
        if n == 0:
            curMin, curMax = 1, 1
            continue


        curMax, curMin = max(n * curMax, n * curMin, n),min(n * curMax, n * curMin, n)

        result = max(curMax, curMin, result)

    return result


nums = [1 , 2, -3, 4]

print(maxProd(nums)) # 4 itself
