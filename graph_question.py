def build_matrix(round_matrix, graph):
    n = len(round_matrix)
    team1 = round_matrix[0:n // 2]
    team2 = round_matrix[n // 2:]
    print("Teams", team1, team2)
    for player1 in team1:
        for player2 in team2:
            print("Player", player1, player2)
            graph[player1 - 1][player2 - 1] = 1
            graph[player2 - 1][player1 - 1] = 1
            # print("graph ", graph)
    return graph


def init_matrix(n):
    rows, cols = (n, n)
    graph = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(n):
        graph[i][i] = 1
    print("Init graph", graph)
    return graph


def rounds_play(n, m, games):

    graph = init_matrix(n)
    for i in range(m):
        graph = build_matrix(games[i], graph)
        print("Graph after round : ", i)
        print(graph)
    print("final graph")
    print(graph)
    return graph


def check_if_full_connected(graph, n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 1:
                return False
    return True


def check(n, m, games):

    graph = rounds_play(n, m, games)
    answer = check_if_full_connected(graph, n)
    print(answer)


def get_test_data():
    from itertools import permutations
    l = list(permutations(range(1, 9)))
    import numpy as np
    arr = np.array(l)
    np.random.shuffle(arr)
    print(list(arr[:5]))


#false
# check(4, 2, [[1, 2, 3, 4], [4, 3, 1, 2]])
#true
check(4, 2, [[1, 2, 3, 4], [1, 3, 2, 4]])

# True
# check(6, 6, [[1, 6, 3, 4, 5, 2], [6, 4, 2, 3, 1, 5], [4, 2, 1, 5, 6, 3],
#              [4, 5, 1, 6, 2, 3], [3, 2, 5, 1, 6, 4], [2, 3, 6, 4, 1, 5]])

#False
# check(6, 6, [[3, 1, 4, 5, 6, 2], [5, 3, 2, 4, 1, 6], [5, 3, 6, 4, 2, 1],
#              [6, 5, 3, 2, 1, 4], [5, 4, 1, 2, 6, 3], [4, 1, 6, 2, 5, 3]])

# get_test_data()

# check(8, 5, [[6, 2 5 3 8 7 4 1], [6 1 5 4 7 2 3 8],
#  [3 2 1 8 5 7 4 6],
#  [4 1 5 3 8 7 6 2],
#  [6 7 2 3 5 8 4 1]])

# check(8, 5, [[3, 7, 6, 1, 5, 4, 2, 8], [6, 8, 4, 7, 3, 2, 1, 5],
#              [[6, 1, 2, 8, 4, 3, 7, 5]], [1, 6, 7, 8, 4, 5, 3, 2],
#              [8, 5, 4, 7, 3, 6, 1, 2]])

# check(4, 2, [[1, 4, 3, 2], [1, 3, 4, 2]])
