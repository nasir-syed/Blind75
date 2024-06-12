def meetings(intervals):

    intervals.sort(key= lambda i: i[0])



    for index in range(1, len(intervals)):
      i1 = intervals[index-1]
      i2 = intervals[index]

      if i1[1] > i2[0]:
          return False

    return True



intervals = [(0,30), (5,10), (15, 25)]

print(meetings(intervals))
