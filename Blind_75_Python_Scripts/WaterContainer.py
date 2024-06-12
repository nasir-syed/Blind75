def maxArea (height):
    res = 0
    l, r = 0, len(height)-1

    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)

        # if height[l] > height[r]:
        #     r -= 1
        #
        # elif height[r] > height[l]:
        #     l += 1
        #
        # else:
        #     l += 1 # if both are the same, l = r, increment any of them, i chose left

        # you can also rewrite the code like so, because your incrementing left anyway
        if height[l] > height[r]:
            r -= 1

        else:
            l += 1

    return res




