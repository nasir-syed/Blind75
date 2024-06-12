def meeting(intervals):

    # what is the maximum number of overlapping meetings at a given time

    start = [i[0] for i in intervals].sort()
    end = [i[1] for i in intervals].sort()


    res, count = 0, 0
    s, e = 0, 0 # two pointers for each of the array

    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1

        res = max(res, count)
    return res




