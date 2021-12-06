#!/usr/bin/env python3

from os import system as sys, name
import flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True


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
    assert all(list(
        map(lambda x: len(x) == len(matrix[0]),
            matrix))), "every matrix's lists needs to be the same length"
    assert type(column) is int and 0 <= column < len(
        matrix[0]), "column argument needs to be an integer (...)"

    col = [row[column] for row in matrix]
    if (0 not in col):  #si il n'y a pas de place dans la colonne
        return matrix, False
    index = len(col) - 1 - col[::-1].index(
        0)  #recup l'index du dernier 0 de la colonne
    matrix[index][
        column] = player  #... pour le remplacer par le jeton du joueur
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
    if ((length := len(liste)) < nbr):
        return 0, 0  #si la taille de la liste est plus petite que la séquence voulu, return 0, 0
    player, counter = 0, 0  #player étant le joueur du jeton analysé, counter étant le compteur de ces jetons à la suite
    for i in range(length):
        num = liste[i]
        if (player != num):
            player, counter = num, 1  #si le jeton est différent du précedent, on réinitialise player et counter
        else:
            counter += bool(
                player
            )  #ajoute 1 (True = 1) au compteur, n'ajoute rien (False = 0) si le jeton vaut 0
        if (counter == nbr):
            return player, i
    return 0, 0


def checkMatrix(matrix, nbr=4):
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
        diagonal = [
            matrix[k][j] for j, k in zip(range(i, width), range(limit))
        ]
        winner, index = fourInRow(diagonal, nbr)
        if (winner): return "diag1", winner, index, index + i

        diagonal = [
            matrix[k][j]
            for j, k in zip(range(i, width), range(limit - 1, -1, -1))
        ]
        winner, index = fourInRow(diagonal, nbr)
        if (winner):
            return "diag2", winner, index + i, index  #coordinates not working

    for i in range(1, length - 1):
        if (length - i >= nbr):
            diagonal = [
                matrix[j][k] for j, k in zip(range(i, length), range(limit))
            ]
            winner, index = fourInRow(diagonal, nbr)
            if (winner): return "diag3", winner, index + i, index

        if (i + 1 >= nbr):
            diagonal = [
                matrix[j][k] for j, k in zip(range(i, -1, -1), range(limit))
            ]
            winner, index = fourInRow(diagonal, nbr)
            if (winner): return "diag4", winner, index + i, index

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
    test = list(
        map(str, range(1, width + 1))
    )  #imprime le numéro au dessus de chaque colonne pour aider les joueurs
    print(f' {" ".join(test)} ')
    #print(f' {"_ " * width}')
    for row in matrice:
        print("|", end="")

        #remplace chaque jeton (et abscence de jeton) de la liste par un 'X' rouge, un 'O' jaune, ou un espace vide
        row = list(
            map(
                lambda x: f'{RED}X{RESET_ALL}|'
                if x == 1 else (f'{YELLOW}O{RESET_ALL}|'
                                if x == 2 else ' |'), row))
        print("".join(row))
    print(f' {" ".join(test)} ')


def getValidToken(token, column_nbr):
    while (not token.isdigit() or not (0 < int(token) < column_nbr + 1)):
        token = input(f'Veuillez insérer un numéro de colonne valide ! : ')
    return token

def board():
    global grille
    grille = [[0 for j in range(7)] for i in range(6)]


grille = [[0 for j in range(7)] for i in range(6)]
#if __name__ == "__main__": main(grille)
joueur, b = 1, 2
winner = 0

if __name__ == "__main__":
    sys('cls' if name == 'nt' else 'clear')

    @app.route('/', methods=['GET'])
    def home():
        return flask.jsonify(grille)

    @app.route('/', methods=['POST'])
    def my_test_endpoint():

        input_json = flask.request.get_json(force=True)
        # force=True, above, is necessary if another developer
        # forgot to set the MIME type to 'application/json'
        inp = input_json
        global grille
        global joueur, b
        grille, played = play(joueur, inp, grille)
        joueur, b = b, joueur

        q, w, e, r = checkMatrix(grille)

        sys('cls' if name == 'nt' else 'clear')
        ##        affichage(grille)
        print(f"Au tour du joueur {joueur}")
        return flask.jsonify(checkMatrix(grille))

    @app.route('/end', methods=['GET'])
    def end():
        board()
        return flask.jsonify("ok")

    app.run()
