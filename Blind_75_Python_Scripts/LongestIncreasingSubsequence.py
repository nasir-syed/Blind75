def lengthOfLIS(nums):
    LIS = [1] * len(nums)

    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

    print(LIS)
    return max(LIS)



nums = [1,2,4,3]
print(lengthOfLIS(nums))