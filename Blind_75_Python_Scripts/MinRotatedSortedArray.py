def search(nums):
    # we're using a type of binary search for this

    result = nums[0]

    l, r, = 0, len(nums)-1

    while l <= r:
        if nums[l] < nums[r]:
            result = min(result,nums[l])

        m = (l+r)//2
        result = min(result, nums[m])

        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1

        return res

