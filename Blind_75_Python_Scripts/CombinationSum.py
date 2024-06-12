def combiSum(candidates, target):
    res = []

    # recursion time

    def dfs (i, cur, total):
        if total == target:
            res.append(cur.copy()) # creating a copy
            return

        if i >= len(candidates) or total > target:
            return


        cur.append(candidates[i])
        print(cur)
        dfs(i, cur, total + candidates[i])
        cur.pop() # popping the last element
        dfs(i + 1, cur, total)


    dfs(0, [], 0)

    return res


nums = [2,3,6,7]
print(combiSum(nums, 7))