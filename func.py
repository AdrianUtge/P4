def play(player, column, matrix):
    #manque les test (assert) pour les arguments
    col = [row[column] for row in matrix]
    index = 5 - col[::-1].index(0) #faire un return au cas où il n'y a plus de place dans la colonne
    matrix[index][column] = player
    return matrix
