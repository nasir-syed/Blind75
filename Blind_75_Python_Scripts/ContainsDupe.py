def containsDupe (nums):
    hashset = set() # creating a hashset

    for n in nums:
        if n in hashset: # if its already in the set, return tru
            return True

        hashset.add(n) # else add it in

    return False # if there were no dupes at all, return False


nums = [2,4,5,2,6,3]

print(containsDupe(nums))