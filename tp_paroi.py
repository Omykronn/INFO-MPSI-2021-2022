from random import randrange
import numpy as np
from matplotlib.pyplot import plot, ion  # Library pas disponible sur Python 3.10


prof1 = [[0, 1, 1, 1, 0, 0, 0],
         [1, 1, 0, 1, 0, 0, 0],
         [0, 1, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 1],
         [0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0],
         [0, 0, 0, 1, 1, 1, 0],
         [0, 1, 0, 0, 0, 0, 0]]


def creeparoi(l: int, c: int, p: float):
    """
    Génère de manière aléatoire une paroi de largeur l et de hauteur c, avec une proportion p de cellules permables

    :param int l: Largeur de la paroi
    :param int c: Hauteur de la paroi
    :param float p: Proportion de cellules perméables
    :return list: Paroi finale
    """
    paroi = [[0 for _ in range(l)] for _ in range(c)]  # Génération d'une paroi totalement imperméable
    nb_perm = 0  # Compteur du nombre de cellules perméables effectives
    goal_perm = int(l * c * p)  # Nombre de cellules perméables à créer

    while nb_perm < goal_perm:
        i, j = randrange(0, c), randrange(0, l)

        if paroi[i][j] == 0:
            paroi[i][j] = 1
            nb_perm += 1

    return paroi


def testparoipermeable(paroi: list):
    """
    Test de la perméabilité de la paroi par simulation

    :param list paroi: Paroi à tester
    :return bool: Booléen en fonction de la perméabilité de la paroi
    """
    height, width = np.shape(paroi)[:2]

    # On mouille la surface extrème-gauche
    for i in range(height):
        if paroi[i][0] == 1:
            paroi[i][0] = 2

    # On étend l'humidité dans la paroi
    for j in range(1, width):
        for i in range(height):
            if paroi[i][j] == 1 and paroi[i][j - 1] == 2:
                # --- On étend sur la même colonne vers le haut
                a = 0

                while i - a >= 0 and paroi[i - a][j] == 1:
                    paroi[i - a][j] = 2
                    a += 1

                    # show(paroi)  # Ligne à décommenter pour voir l'évolution

                # --- On étend sur la même colonne vers le bas
                a = 1  # La cellule (i; j) est déjà mouillée

                while i + a < height and paroi[i + a][j] == 1:
                    paroi[i + a][j] = 2
                    a += 1

                    # show(paroi)  # Ligne à décommenter pour voir l'évolution

    # Test de la permeabilité

    permeable = False
    i = 0

    while i < height and not permeable:
        permeable = paroi[i][-1] == 2
        i += 1

    return permeable


def simulation(l: int, c: int, n: int, lp: list, fonction_test=testparoipermeable):
    """
    Simule, pour chaque valeur p dans lp, n parois de dimensions l×c

    :param int l: Largeur des parois
    :param int c: Hauteur des parois
    :param int n: Nombre de parois à simuler pour chaque valeur de lp
    :param list lp: Liste des indices d'imperfection
    :param function fonction_test: Fonction de test à utiliser (par défaut : testparoipermeable())
    :return list: Liste des proportions de parois perméables pour chaque valeur de lp
    """
    result = []

    for p in lp:
        nb_perm = 0

        for _ in range(n):
            if fonction_test(creeparoi(l, c, p)):
                nb_perm += 1

        result.append(nb_perm / n)

    return result


def graph():
    """
    Affiche le graphique des données calculées par simulation() selon des données particulières

    :return: None
    """
    t = [0, 0.5, 0.52, 0.54, 0.56, 0.58, 0.6, 0.62, 0.65, 1]
    d = simulation(100, 50, 200, t)
    ion()
    plot(t, d, color="black")


# ------ FONCTION EN PLUS ------


def show(paroi: list):
    """
    Affiche une répresentation graphique d'une paroi

    :param list paroi: Tableau Représentatif d'une paroi
    :return: None
    """
    for line in paroi:
        for cell in line:
            if cell == 0:
                print("█", end="")
            elif cell == 1:
                print("░", end="")
            else:
                print("×", end="")
        print("")
    print("\n")
