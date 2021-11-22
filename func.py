def play(player, column, matrix):
    #manque les test (assert) pour les arguments
    assert type(player) is int, "player argument needs to be an integer"
    assert type(matrix) is list, "matrix argument needs to be a list"
    assert all(list(map(lambda x: len(x) == len(matrix[0]), matrix))), "every matrix's lists needs to be the same length"
    assert type(column) is int and 0 <= column < len(matrix[0]), "column argument needs to be an integer (...)"

    col = [row[column] for row in matrix]
    if (0 not in col):
        return matrix, False
    index = 5 - col[::-1].index(0)
    matrix[index][column] = player
    return matrix, True

def fourInRow(liste):
    a, b = 0, 0
    for i in liste:
        if (a != i): a, b = i, 1
        else: b += bool(a)
        if (b == 4):
            return a
    return 0

def CheckDiag(col):
    print("Checking Diagonal", col)
    for j in range(6):
        if (col[1][j] == 1 and col[0][j + 1] == 1):
            print("Diagonal Detected")
        if (col[0][j] == 1 and col[1][j + 1] == 1):
            print("Diagonal Detected")
    print("Diagonal Check Complete")
