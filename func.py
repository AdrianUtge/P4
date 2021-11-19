def play(player, column, matrix):
    #manque les test (assert) pour les arguments
    col = [row[column] for row in matrix]
    if (0 not in col):
        return matrix, False
    index = 5 - col[::-1].index(0)
    matrix[index][column] = player
    return matrix, True


def CheckDiag(col):
    print("Checking Diagonal", col)
    for j in range(6):
        if (col[1][j] == 1 and col[0][j + 1] == 1):
            print("Diagonal Detected")
        if (col[0][j] == 1 and col[1][j + 1] == 1):
            print("Diagonal Detected")
    print("Diagonal Check Complete")
