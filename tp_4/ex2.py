def indice_dans(L: list, x: int):
    """
    Renvoie l'indice de l'élément x dans la liste L triée, suite à une dichotomie

    :param list L: Liste triée
    :param int x: Élément de la liste L
    :return int i_moy: Indice de l'élément x dans la liste L
    """
    i_max = len(L) - 1
    i_min = 0
    i_moy = len(L) // 2

    while L[i_moy] != x:        
        if x < L[i_moy]:
            i_max = i_moy - 1
        else:
            i_min = i_moy + 1

        i_moy = (i_min + i_max) // 2

    return i_moy
