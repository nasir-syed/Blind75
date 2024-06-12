def merge(intervals):

    intervals.sort(key = lambda i: i[0]) # sorting by start value

    output = [intervals[0]] # add the first interval to the output

    for start, end in intervals[1:]:
        lastEnd = output[-1][1] # the ending element of the lastly added interval

        if start <= lastEnd: # it will then fall within the range
            output[-1][1] = max(lastEnd, end)

        else:
            output.append([start, end])


    return output


