def twoSum (nums, target):

    prevMap = {} #hashmap, val : index

    for i, n in enumerate(nums):
        # with enumerate we can store the index of the element in variable

        diff = target - n # get the difference from the target, and see if its in the map

        if diff in prevMap:
            return [prevMap[diff], i] # return the index fo the element in the hashmap
                                      # and the element in the list, not added to the map

        prevMap[n] = i  # if the diff is not in the hashmap, add the element to the hashmap

    return


nums = [2, 4, 5, 3, 9]

print(twoSum(nums, 5))


