

def maxSubArray(nums):
    maxSub = nums[0]
    curSum = 0
    track = [] # don't really need it, just to learn

    for n in nums:
        if curSum < 0:
            curSum = 0 # we discard any negative perfixes
        curSum += n
        maxSub = max(maxSub, curSum)
        track.append(curSum)


    return maxSub

nums = [-2, 1, -3, 4, -1, 2 ,1, -5, 4]

print(maxSubArray(nums))