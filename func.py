#!/usr/bin/env -S python3 -i

import flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True


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


def fourInRow(liste, nbr=4):
    if ((length := len(liste)) < nbr): return 0, 0
    player, counter = 0, 0
    for i in range(length):
        num = liste[i]
        if (player != num): player, counter = num, 1
        else: counter += bool(player)
        if (counter == nbr):
            return player, i
    return 0, 0


##################################
#fonctions provisoire, utiliser pour simplifier les test
from random import randint
def mat():
    return [[randint(0,2) for i in range(7)] for j in range(6)]
def pri(t):
    for i in t: print(i)
def test(a):
    for i in range(a):
        t = mat()
        test = checkMatrix(t)
        print(test)
        if test[1]:
            print("####################################################################")
        pri(t)
####################################


def checkMatrix(matrix, nbr = 4):
    """ the function returns a tuple constitued of A, B, C, D:
    A is string being the "type" of sequence, either in a row, a column, an up-left to down-right diagonal (diag1) or an up-right to down-left diagonal (diag2)
    B is the number of the player who won
    C and D are the coordinates of the last token of the connect4 (puissance 4)"""

    length = len(matrix)
    width = len(matrix[0])
    for i in range(length):
        winner, index = fourInRow(matrix[i], nbr)
        if (winner): return "row", winner, i, index

    for i in range(width):
        col = [matrix[j][i] for j in range(length)]
        winner, index = fourInRow(col, nbr)
        if (winner): return "col", winner, index, i

    #seriously needs to be upgraded, such as returned coordinates, returned sequence type and upgrade the bad usage of for loops 
    for i in range(length):
        diagonal = [matrix[j][j - i] for j in range(i, length)]
        winner, index = fourInRow(diagonal, nbr)
        if (winner): return "diag1", winner, index+i, index

        diagonal = [matrix[j][length + i - j] for j in range(i, length)]
        winner, index = fourInRow(diagonal, nbr)
        if (winner): return "diag2", winner, index+i, index #coordinates not working

        diagonal = [matrix[j][i - j] for j in range(i, -1, -1)]
        winner, index = fourInRow(diagonal, nbr)
        if (winner): return "diag3", winner, index+i, index #coordinates not working


        diagonal = [matrix[j][length - i + j] for j in range(i, -1, -1)]
        winner, index = fourInRow(diagonal, nbr)
        if (winner): return "diag4", winner, index+i, index #coordinates not working

    return "none", 0, 0, 0


def CheckDiag(col):
    print("Checking Diagonal", col)
    for j in range(6):
        if (col[1][j] == 1 and col[0][j + 1] == 1):
            print("Diagonal Detected")
        if (col[0][j] == 1 and col[1][j + 1] == 1):
            print("Diagonal Detected")
    print("Diagonal Check Complete")


def checkifcollumavailable(board, col):
    for row in board:
        if row[col] == 0:
            return True
    return False


####################################
#Api il faut juste ramplacer board par la variable de la table


@app.route('/', methods=['GET'])
def home():
    return flask.jsonify(board)


@app.route('/', methods=['POST'])
def my_test_endpoint():
    input_json = flask.request.get_json(force=True)
    # force=True, above, is necessary if another developer
    # forgot to set the MIME type to 'application/json'
    inp = input_json
    print(inp)
    if checkifcollumavailable(board, inp) == True:
        dictToReturn = True
    else:
        dictToReturn = False
    return flask.jsonify(dictToReturn)


if __name__ == '__main__':
    app.run(debug=True)
app.run()
