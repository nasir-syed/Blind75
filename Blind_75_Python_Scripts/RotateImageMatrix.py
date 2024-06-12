def rotate (matrix):
    l , r = 0, len(matrix) - 1

    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            # save the top left value
            topLeft = matrix[top][l + i]

            # move bottom left into top left
            matrix[top][l + i] = matrix[bottom - i][l]


            # move bottom right to bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # move top right to bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            # move top left to top right
            matrix[top + i][r] = topLeft

        r -= 1 # will make us move down
        l += 1 # will make us move to the right


mat = [[1 , 2 , 3], [4, 5, 6], [7, 8, 9]]
rotate(mat)
print(mat)