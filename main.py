#!/usr/bin/env python3

from colorama import Back as ba, Style as st
from os import system as sys, name

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
def mat(a = 7, b = 6):
    return [[randint(0,2) for i in range(a)] for j in range(b)]
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
    limit = min(length, width)
    for i in range(length):
        winner, index = fourInRow(matrix[i], nbr)
        if (winner): return "row", winner, i, index

    for i in range(width):
        col = [matrix[j][i] for j in range(length)]
        winner, index = fourInRow(col, nbr)
        if (winner): return "col", winner, index, i

    #seriously needs to be upgraded, such as returned coordinates, returned sequence type and upgrade the bad usage of for loops 
    for i in range(width - nbr + 1):
        diagonal = [matrix[k][j] for j, k in zip(range(i, width), range(limit))]
        winner, index = fourInRow(diagonal, nbr)
        if (winner): return "diag1", winner, index, index+i

        diagonal = [matrix[k][j] for j, k in zip(range(i, width), range(limit-1, -1, -1))]
        winner, index = fourInRow(diagonal, nbr)
        if (winner): return "diag2", winner, index+i, index #coordinates not working

    for i in range(1, length - 1):
        if (length - i >= nbr):
            diagonal = [matrix[j][k] for j, k in zip(range(i, length), range(limit))]
            winner, index = fourInRow(diagonal, nbr)
            if (winner): return "diag3", winner, index+i, index

        if (i + 1 >= nbr):
            diagonal = [matrix[j][k] for j, k in zip(range(i, -1, -1), range(limit))]
            winner, index = fourInRow(diagonal, nbr)
            if (winner): return "diag4", winner, index+i, index

    return "none", 0, 0, 0


def affichage(matrice):
    width = len(matrice[0])
    test = list(map(str, range(1, width+1)))
    print(f' {" ".join(test)} ')
    #print(f' {"_ " * width}')
    for row in matrice:
        print("|", end="")
        row = list(map(lambda x: f'{ba.RED}X{st.RESET_ALL}|' if x == 1 else (f'{ba.YELLOW}O{st.RESET_ALL}|' if x == 2 else ' |'), row))
        print("".join(row))
    print(f' {" ".join(test)} ')


def main():
    sys('cls' if name == 'nt' else 'clear')
    grille = [[0 for j in range(7)] for i in range(6)]
    joueur, b = 1, 2
    winner = 0
    while (winner == 0 and any(map(lambda row: 0 in row, grille))):
        print("PUISSANCE 4\n")
        affichage(grille)
        
        #input hell
        colonne = input(f'\nJoueur {joueur}, indiquer la colonne où placer votre jeton : ')
        while (not colonne.isdigit() or not (0 < int(colonne) < 8)):
            colonne = input(f'Veuillez insérer un numéro de colonne valide ! : ')
        
        colonne = int(colonne) - 1    
        grille, played = play(joueur, colonne, grille)
        while (not played):
            colonne = input(f'La colonne est déjà remplie, réinsérer un autre numéro de colonne : ')
            while (not colonne.isdigit() or not (0 < int(colonne) < 8)):
                colonne = input(f'Veuillez insérer un numéro de colonne valide ! : ')
            colonne = int(colonne) - 1    
            grille, played = play(joueur, colonne, grille)
 
        seq, winner, x, y = checkMatrix(grille)
        joueur, b = b, joueur
        sys('cls' if name == 'nt' else 'clear')

    print("PUISSANCE 4\n")
    affichage(grille)
    if (winner):
        return print(f"\nLe gagnant est le joueur {winner}")
    print("\nAucun des joueurs n'a gagner !")

if __name__ == "__main__": main()
