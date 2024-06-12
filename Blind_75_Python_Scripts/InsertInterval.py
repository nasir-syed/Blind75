def insert(intervals, newInterval):

    res = []

    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
        # end value of the new interval
        # is smaller than the start value of the current interval

            res.append(newInterval)
            return res + intervals[i:] # adding the remaining intervals

        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])

        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

    res.append(newInterval)

    return res


