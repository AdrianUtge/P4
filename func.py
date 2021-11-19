def play(player, column, matrix):
    #manque les test (assert) pour les arguments
    col = [row[column] for row in matrix]
    if (0 not in col):
        return matrix, False
    index = 5 - col[::-1].index(0) 
    matrix[index][column] = player
    return matrix, True
