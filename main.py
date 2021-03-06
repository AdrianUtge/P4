#!/usr/bin/env python3

from os import system as sys, name

def play(player, column, matrix):
    """
        ...
        return new_matrix, played_bool

    "Ajoute" un jeton du joueur (player) indiqué dans la colonne (column) d'une grille (matrix) de jeu Puissance 4.
    Retourne la grille de base et False si il n'y avaut okys de place dans la colonne, sinon renvoie la nouvelle matrice et True.

    Paramètres:
        - player (any): variable correspondant au jeton du joueur
        - column (int): entier correspondant au numéro de la colonne où ajouter le jeton
        - matrix (list): une liste de liste (matrice) correspondant à la grille de jeu, les listes doivent être de taille égale
    """
    assert type(matrix) is list and type(matrix[0]) is list, "l'argument de matrix doit être une liste de listes"
    assert all(map(lambda x: len(x) == len(matrix[0]), matrix)), "tout les liste de l'argument de matrix doivent avoir la même taille"
    assert type(column) is int and 0 <= column < len(matrix[0]), "l'argument de column doit être un numéro de colonne valide de la grille."

    col = [row[column] for row in matrix]

    if (0 not in col): #si il n'y a pas de place dans la colonne
        return matrix, False 

    #récupère l'index du dernier 0 de la colonne
    col = col[::-1] #inverse la colonne
    index = col.index(0)
    index = len(col) - 1 - index 

    matrix[index][column] = player #... pour le remplacer par le jeton du joueur
    return matrix, True


def gagner(liste, nbr=4):
    """
    vérifie si il y'a un certain nombre de jeton consécutif dans une liste
    """
    assert type(liste) is list
    assert type(nbr) is int

    joueur  = 0
    compteur = 0
    for i in range(len(liste)):
        jeton = liste[i]

        if (joueur != jeton): 
            joueur = jeton
            compteur = 1
        elif (joueur == 1 or joueur == 2):
            compteur += 1

        if (compteur == nbr):
            return joueur, i
    return 0, 0


def checkMatrix(matrix, nbr = 4):
    """ 
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
    assert type(matrix) is list and type(matrix[0]) is list, "l'argument de matrix doit être une liste de listes"
    assert all(map(lambda x: len(x) == len(matrix[0]), matrix)), "tout les liste de l'argument de matrix doivent avoir la même taille"
    assert type(nbr) is int, "l'argument de nbr doit être une entier" #utile seulement si une autre valeur a été donner en argument

    longueur = len(matrix)
    largeur = len(matrix[0])

    #lignes
    for i in range(longueur):
        winner, index = gagner(matrix[i], nbr)
        if (winner): return "row", winner, i, index

    #colonnes
    for i in range(largeur):
        col = [matrix[j][i] for j in range(longueur)]
        winner, index = gagner(col, nbr)
        if (winner): return "col", winner, index, i

    #diagonales
    limit = min(longueur, largeur)
    for i in range(largeur - nbr + 1):
        diagonal = [matrix[k][j] for j, k in zip(range(i, largeur), range(limit))]
        winner, index = gagner(diagonal, nbr)
        if (winner): return "diag1", winner, index, index+i

        diagonal = [matrix[k][j] for j, k in zip(range(i, largeur), range(limit-1, -1, -1))]
        winner, index = gagner(diagonal, nbr)
        if (winner): return "diag2", winner, index+i, index #coordinates not working

    for i in range(1, longueur - 1):
        if (longueur - i >= nbr):
            diagonal = [matrix[j][k] for j, k in zip(range(i, longueur), range(limit))]
            winner, index = gagner(diagonal, nbr)
            if (winner): return "diag3", winner, index+i, index

        if (i + 1 >= nbr):
            diagonal = [matrix[j][k] for j, k in zip(range(i, -1, -1), range(limit))]
            winner, index = gagner(diagonal, nbr)
            if (winner): return "diag4", winner, index+i, index

    return "none", 0, 0, 0


def affichage(matrice):
    """
        ...
        return None

    Affiche la grille de jeu dans le shell, en remplaçant les 1 par des 'X' rouge et les 2 par des 'O' jaune.

    Paramètres:
        - matrice (list): la grille de jeu à afficher, doit être une liste de liste.
    """
    assert type(matrice) is list and type(matrice[0]) is list, "l'argument de matrice doit être une liste de listes"
    assert all(map(lambda x: len(x) == len(matrice[0]), matrice)), "tout les liste de l'argument de matrice doivent avoir la même taille"

    #code d'échappement ANSI permettant la coloration des jeton (c'est plus joli comme ça :D )
    RED = '\x1b[41m'
    YELLOW = '\x1b[43m'
    RESET_ALL = '\x1b[0m'

    width = len(matrice[0])
    test = list(map(str, range(1, width+1)))
    print(' ' + " ".join(test)) #imprime le numéro au dessus de chaque colonne pour aider les joueurs
    #print(f' {"_ " * width}')
    for row in matrice:
        print("|", end="")

        #remplace chaque jeton (et abscence de jeton) de la liste par un 'X' rouge, un 'O' jaune, ou un espace vide
        row = list(map(lambda x: f'{RED}X{RESET_ALL}|' if x == 1 else (f'{YELLOW}O{RESET_ALL}|' if x == 2 else ' |'), row))
        print("".join(row))
    print(f' {" ".join(test)} ')


def getValidToken(token, column_nbr): #utilisé pour simplifier un peu le code dans le main()
    """ 
        ... return valid_token_nbr

    Vérifie si l'input de l'utilisateur est bien un nombre entier naturel non nulle, sinon redemande une nouvelle input.

    Paramètres:
        - token (str): le précédent input de l'utilisateur qui sera vérifié
        - column_nbr (int): le nombre de colonnes de la grille
    """
    while (not token.isdigit() or not (0 < int(token) < column_nbr + 1)):
        token = input(f'Veuillez insérer un numéro de colonne valide ! : ')
    return token
    

def main():
    """Programme principale"""

    sys('cls' if name == 'nt' else 'clear') #nettoie tout le terminal dès le début, et le refait à chaque tour (c'est encore plus joli :D )

    grille = [[0 for j in range(7)] for i in range(6)]
    joueur, b = 1, 2 #les numéros des deux joueurs, à chaque tour on inverse les deux numéros
    winner = 0

    #any(map(lambda row: 0 in row, grille))
    nbrTours = 42 #le nombre maxium de tour possible
    while (winner == 0 and nbrTours != 0): #tant qu'il y a pas de gagnant et que le jeu n'est pas finie
        print("PUISSANCE 4\n")
        affichage(grille) #waaaaaaa :)
        
        colonne = input(f'\nJoueur {joueur} ({"X" if joueur == 1 else "O"}), indiquer la colonne où placer votre jeton : ')
        colonne = int(getValidToken(colonne, 7)) - 1

        grille, played = play(joueur, colonne, grille)
        while (not played):
            colonne = input(f'La colonne est déjà remplie, réinsérer un autre numéro de colonne : ')
            colonne = int(getValidToken(colonne, 7)) - 1
            grille, played = play(joueur, colonne, grille)
        
        winner = checkMatrix(grille)[1] #recheche de séquence dans la grille 

        joueur, b = b, joueur #inversions des deux joueurs pour la prochaine itération de la boucle
        nbrTours -= 1
        sys('cls' if name == 'nt' else 'clear') #et on renettoie  

    print("PUISSANCE 4\n")
    affichage(grille)

    if (winner):
        print(f"\nLe gagnant est le joueur {winner}")
    else:
        print("\nAucun des joueurs n'a gagner !")

if __name__ == "__main__": main()
