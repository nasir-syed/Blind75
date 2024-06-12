def kthSmallest(root):
    n = 0
    stack = []
    cur = root

    while cur and stack:

        # go left as much as possible until cur is not null
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop() # remove the recently added value and update cur
        n += 1

        if n == k:
            return cur.val

        cur = cur.right
