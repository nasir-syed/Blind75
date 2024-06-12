def overlap(intervals):

    intervals.sort()


    res = 0 # we have return the count of how many we need to delete
    

    prevEnd = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end

        else:
            res += 1
            prevEnd = min(end, prevEnd)

    return res

