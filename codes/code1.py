def skipNumbers(x, y, numbers):
    toSkip = 0

    for i in range(len(numbers)):
        num = numbers[i]
        if num > x and num > y:
            toSkip += 1
            continue
        if x >= y:
            x = x - num
        else:
            y = y - num

    print(toSkip)

    return toSkip


numbers = [
    6094, 2008, 8953, 185, 6030, 2478, 7164, 4126, 7, 4837, 4933, 1439, 4477,
    2134, 3938, 5868, 11, 11, 3, 8891, 1, 699, 6130, 9015, 5091, 11, 2294, 471,
    1316, 3, 4075, 11, 2442, 1621, 1291, 8307, 7792, 8380, 1610, 2256, 5, 6907,
    3, 8528, 2555, 3341, 3162, 7708, 5066, 1920, 3426, 3436, 7182, 4, 4052,
    3052, 6138, 5, 6228, 8426, 24, 1124, 82, 97, 1943, 14, 1491, 9901, 11,
    6691, 1, 2888, 2, 9817, 4900, 4522
]
x = 75
y = 75
# a = skipNumbers(x, y, numbers)
# print(a)


def solutionPack(packs, containers):
    map = {}
    result = []

    for pack in packs:
        found = False
        for idx in range(len(containers)):
            if idx not in map and pack <= containers[idx]:
                result.append(idx)
                map[idx] = True
                found = True
                break
        if not found:
            result.append(-1)

    return result


packs = [10000, 10, 1, 1]
packs = [12, 5, 5]
containers = [12, 12, 1, 1]
containers = [5, 4, 15, 3]
# a = solutionPack(
#     packs,
#     containers,
# )
# print(a)


def findSubmatrices(rows, cols, black):
    ans = [0] * 5
    if (rows < 2 or cols < 2):
        return ans

    grid = [[0 for c in range(cols)] for r in range(rows)]

    print(grid)
    for row in black:
        grid[row[0]][row[1]] = 1

    for i in range(0, rows - 1):
        for j in range(0, cols - 1):
            nums_black = grid[i][j] + grid[i][j + 1] + grid[i + 1][j] + grid[
                i + 1][j + 1]
            ans[nums_black] += 1

    return ans


black = [[0, 0], [0, 1], [1, 0]]
rows = 3
cols = 3

a = findSubmatrices(rows, cols, black)
print(a)