

def missingNum(nums):

    # res = int((len(nums)*(len(nums)+1))/2) # get sum of all elements (including missing number)
    #
    # for n in nums:
    #     res -= n # subtract the value of each element in the list
    #     # the remainder is the missing element
    #
    # return res

    # how neetcode did it

    res = len(nums)

    for i in range(len(nums)):
        res += (i - nums[i])

    return res


nums = [0, 1, 2, 4]
print(missingNum(nums))

