'''
https://www.algoexpert.io/questions/spiral-traverse

Solve it simply based on logic. Move right then down then left and up
'''


def spiralTraverse(arr):

    row = len(arr)
    col = len(arr[0])
    visited = []
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(0)
        visited.append(temp)

    print(visited)

    isPresent = True
    result = []
    i = 0  # index
    j = 0  # index
    while (isPresent):
        isPresent = False
        while (j < col and visited[i][j] == 0):
            print("Cond 1")
            print(i, j)
            print(arr[i][j])
            print("----")
            result.append(arr[i][j])
            visited[i][j] = 1
            j += 1
            isPresent = True
        j = j - 1
        i = i + 1
        while (i < row and visited[i][j] == 0):
            print("Cond 2")
            print(i, j)
            print(arr[i][j])
            print("----")
            result.append(arr[i][j])
            visited[i][j] = 1
            i += 1
            isPresent = True
        i = i - 1
        j = j - 1
        while (j >= 0 and visited[i][j] == 0):
            print("Cond 3")
            print(i, j)
            print(arr[i][j])
            print("----")
            result.append(arr[i][j])
            visited[i][j] = 1
            j = j - 1
            isPresent = True
        j = j + 1
        i = i - 1
        while (i >= 0 and visited[i][j] == 0):
            print("Cond 4")
            print(i, j)
            print(arr[i][j])
            print("----")
            result.append(arr[i][j])
            visited[i][j] = 1
            i = i - 1
            isPresent = True
        i = i + 1
        j = j + 1

    return result


arr = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
print(spiralTraverse(arr))