#!/usr/bin/env python3

#from colorama import Back as ba, Style as st
from os import system as sys, name

def play(player, column, matrix):
    """
    play(player, column, matrix):
        ...
        return new_matrix, played_bool

    "Ajoute" un jeton du joueur (player) indiqué dans la colonne (column) d'une grille (matrix) de jeu Puissance 4.
    Retourne la grille de base et False si il n'y avaut okys de place dans la colonne, sinon renvoie la nouvelle matrice et True.

    Paramètres:
        - player (int): entier correspondant au numéro du joueur
        - column (int): entier correspondant au numéro de la colonne où ajouter le jeton
        - matrix (list): une liste de liste (matrice) correspondant à la grille de jeu, les listes doivent être de taille égale
    """
    assert type(player) is int, "player argument needs to be an integer"
    assert type(matrix) is list, "matrix argument needs to be a list"
    assert all(list(map(lambda x: len(x) == len(matrix[0]), matrix))), "every matrix's lists needs to be the same length"
    assert type(column) is int and 0 <= column < len(matrix[0]), "column argument needs to be an integer (...)"

    col = [row[column] for row in matrix]
    if (0 not in col): #si il n'y a pas de place dans la colonne
        return matrix, False 
    index = 5 - col[::-1].index(0) #recup l'index du dernier 0 de la colonne
    matrix[index][column] = player #... pour le remplacer par le jeton du joueur
    return matrix, True


def fourInRow(liste, nbr=4):
    """
    fourInRow(liste [, nbr]):
        ...
        return winner, index_of_last_token

    Vérifie si il y'a un nombre indiquée (nbr) de jeton consécutif dans la liste (liste) donnée
    Retourne le gagnant et l'index du dernier jeton de la séquence, sinon retourne 0, 0

    Paramètres:
        - liste (list): la liste où trouver la suite de jeton, l'entier 0 est compris comme l'absence de jeton
        - nbr (int): le nombre indiquant la séquence de jeton voulue
            -> valeur par défaut: 4
    """
    if ((length := len(liste)) < nbr): return 0, 0 #si la taille de la liste est plus petite que la séquence voulu, return 0, 0
    player, counter = 0, 0 #player étant le joueur du jeton analysé, counter étant le compteur de ces jetons à la suite
    for i in range(length):
        num = liste[i]
        if (player != num): player, counter = num, 1 #si le jeton est différent du précedent, on réinitialise player et counter
        else: counter += bool(player) #ajoute 1 (True = 1) au compteur, n'ajoute rien (False = 0) si le jeton vaut 0
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
    """ 
    checkMatrix(matrix, [nbr]):
        ...
        return type_of_sequence, winner, indexX, indexY

    Vérifie si il y'a un nombre indiquée (nbr) de jeton consécutif dans tout la grille de jeu (matrix) indiqué
    Si il y a un gagnant, retourne le type de séquence trouvé (colonne, ligne ou diagonale), le numéro du joueur gagnant
        , et l'index dans la matrice du dernier jeton de la séquence (ne marhche pas pour les diagonales)
    Renvoie "none", 0, 0, 0 si la fonction n'a pas trouvé de séquence.

    Paramètres:
        - matrix (list): une liste de liste correspondant à la grille du jeu, doit être consituté de liste de tailles égaux
        - nbr (int): le nombre indiquant la longueur de la séquence recherché
            -> valeur par défaut: 4
    """


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


    #gros bordel, flemme d'expliquer, vous  me demandrez IRL

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
    """
    affichage(matrice):
        #doesn't return anything

    Affiche la grille de jeu dans le shell, en remplaçant les 1 par des 'X' rouge et les 2 par des 'O' jaune.

    Paramètres:
        - matrice (list): la grille de jeu à afficher, doit être une liste de liste.
    """

    #code d'échappement ANSI permettant la coloration des jeton (c'est plus joli comme ça :D )
    RED = '\x1b[41m'
    YELLOW = '\x1b[43m'
    RESET_ALL = '\x1b[0m'

    width = len(matrice[0])
    test = list(map(str, range(1, width+1))) #imprime le numéro au dessus de chaque colonne pour aider les joueurs
    print(f' {" ".join(test)} ')
    #print(f' {"_ " * width}')
    for row in matrice:
        print("|", end="")

        #remplace chaque jeton (et abscence de jeton) de la liste par un 'X' rouge, un 'O' jaune, ou un espace vide
        row = list(map(lambda x: f'{RED}X{RESET_ALL}|' if x == 1 else (f'{YELLOW}O{RESET_ALL}|' if x == 2 else ' |'), row))
        print("".join(row))
    print(f' {" ".join(test)} ')


def main():
    """Programme principale"""

    sys('cls' if name == 'nt' else 'clear') #nettoie tout le terminal dès le début, et le refait à chaque tour (c'est encore plus joli :D )
    grille = [[0 for j in range(7)] for i in range(6)]
    joueur, b = 1, 2 #les numéros des deux joueurs, à chaque tour on inverse les deux numéros
    winner = 0
    while (winner == 0 and any(map(lambda row: 0 in row, grille))): #tant qu'il y a pas de gagnant et qu'il y'a encore de la place dans la grille
        print("PUISSANCE 4\n")
        affichage(grille) #waaaaaaa :)
        
        #input hell ################################
        colonne = input(f'\nJoueur {joueur} ({"X" if joueur == 1 else "O"}), indiquer la colonne où placer votre jeton : ')
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
        #fin de l'input hell ########################
        #probablement à remplacer si on veut un beau gui
        
        seq, winner, x, y = checkMatrix(grille) #recheche de séquence dans la grille 
        joueur, b = b, joueur #inversions des deux joueurs pour la prochaine itération de la boucle
        sys('cls' if name == 'nt' else 'clear') #et on renettoie  

    print("PUISSANCE 4\n")
    affichage(grille)
    if (winner):
        return print(f"\nLe gagnant est le joueur {winner}")
    print("\nAucun des joueurs n'a gagner !")

if __name__ == "__main__": main()
