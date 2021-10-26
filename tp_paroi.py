from random import randrange


def creeparoi(l: int, c: int, p: float):
    """
    Génère de manière aléatoire une paroi de largeur l et de hauteur c, avec une proportion p de cellules permables

    :param int l: Largeur de la paroi
    :param int c: Hauteur de la paroi
    :param float p: Proportion de cellules perméables
    :return list: Paroi finale
    """
    paroi = [[0 for j in range(l)] for i in range(c)]  # Génération d'une paroi totalement imperméable
    nb_perm = 0  # Compteur du nombre de cellules perméables effectives
    goal_perm = int(l * c * p)  # Nombre de cellules perméables à créer

    while nb_perm < goal_perm:
        i, j = randrange(0, c), randrange(0, l)

        if paroi[i][j] == 0:
            paroi[i][j] = 1
            nb_perm += 1

    return paroi


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
            else:
                print("░", end="")
        print("")
