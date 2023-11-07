'''
https://leetcode.com/problems/set-matrix-zeroes/
'''


# O(m*n) space complexity worst case
def setZeroes(matrix):
    zeroes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zeroes.append([i, j])

    counter = 0
    # print("zeroes ", zeroes)
    while (counter < len(zeroes)):
        row, col = zeroes[counter]

        #set everything in row as zero

        for j in range(col, len(matrix[0])):
            matrix[row][j] = 0

        for j in reversed(range(col)):
            matrix[row][j] = 0

        # set everything in column as zero

        for i in range(row, len(matrix)):
            matrix[i][col] = 0

        for i in reversed(range(row)):
            matrix[i][col] = 0

        # print("Matrix : ", matrix)
        counter += 1

    return matrix


'''
Instead of storing all the indices, we can just store the row and col as separate sets. That is for all indices in row having zero, store row number only and for all indices in column , store column number only.
Use set to remove duplicates. So we will max store only (m+n) values only
'''


#best approach with m+n space complexity
def setZeroesMN(matrix):
    row_set = set()
    col_set = set()
    ROW = len(matrix)
    COL = len(matrix[0])
    for i in range(ROW):
        for j in range(COL):
            if matrix[i][j] == 0:
                row_set.add(i)
                col_set.add(j)

    print(row_set)
    print(col_set)
    counter = 0
    row_list = list(row_set)
    while (counter < len(row_list)):
        row = row_list[counter]
        for j in range(0, COL):
            matrix[row][j] = 0
        counter += 1

    counter = 0
    col_list = list(col_set)
    while (counter < len(col_list)):
        col = col_list[counter]
        for i in range(0, ROW):
            matrix[i][col] = 0
        counter += 1

    return matrix


# better on space complexity but high on time complexity
def setZeroesMPlusN(matrix):
    row_set = -1
    col_set = -1
    ROW = len(matrix)
    COL = len(matrix[0])
    for i in range(ROW):
        for j in range(COL):
            if matrix[i][j] == 0:
                row = i
                for k in range(0, COL):
                    if matrix[row][k] != 0:
                        matrix[row][k] = '-1'
                col = j
                for k in range(0, ROW):
                    if matrix[k][col] != 0:
                        matrix[k][col] = '-1'
                # print(matrix)

    for i in range(ROW):
        for j in range(COL):
            if matrix[i][j] == '-1':
                matrix[i][j] = 0
    return matrix


# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

print(setZeroesMPlusN(matrix))