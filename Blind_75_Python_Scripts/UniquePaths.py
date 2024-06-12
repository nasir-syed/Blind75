def ways(m, n): # columns, rows
    row = [1] * n #initially the bottom row

    for i in range(m - 1): # go thru all rows except last one
        newRow = [1] * n # new row same dimensions
        for j in range(n - 2, -1, -1):
            newRow[j] = newRow[j+1] + row[j] # the value to the right + bottom
        row = newRow # set the old row to the newRow

    return row[0]

print(ways(7, 3))


