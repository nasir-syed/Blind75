

def prod(nums):
    result = [1] * (len(nums))  # creating a output array == length of nums
    # and in each position 1 is stored currently

    prefix = 1

    for i in range(len(nums)):
        result[i] = prefix
        print("prefix: ", prefix)
        prefix *= nums[i]

    postfix = 1

    # we start at the end of the array and go to the beginning
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        print("postfix: ", postfix)
        postfix *= nums[i]


    return result


nums = [1,2,3,4]
print(prod(nums))