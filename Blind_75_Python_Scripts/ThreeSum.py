def threeSum(nums):

    res = []
    nums.sort() #sort the array

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            # if the next a element is same as the previous, skip it
            continue

        l, r = i+1, len(nums)-1
        # left and right pointer for the two other values we need

        # l must not equal to r, we need two seperate values
        while l < r:
            # sum of all three elements should equal 0
            threeSum = a + nums[l] + nums[r]

            # if the sum of the elements is greater than 0, and the array is sorted,
            # so to get a lower sum we need decrement the right pointer
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                # if it is equal to 0, append it, and we'll find the next set that may equal 0
                res.append([a, nums[l], nums[r]])

                # increment only the left operator, then the sum will be > 0, so
                # the right operator will be decremented by itself
                l += 1
                while nums[l] == nums [l-1] and l < r:
                    l += 1

    return res