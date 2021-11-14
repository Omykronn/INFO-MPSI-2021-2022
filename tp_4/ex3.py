def existe_dans(L: list, x: int):
    """
    Retourne un couple d'un booléen (si x est dans L) et de l'indice de l'élément le plus proche de x

    :param L: Liste
    :param int x: Élément à chercher dans L
    :return tuple: Booléen convenant à la présence ou non de l'élément x dans la liste L + indice de l'élément le plus
                   proche (indice exact si x existe dans la liste
    """
    i_max = len(L) - 1
    i_min = 0
    i_moy = len(L) // 2

    while L[i_moy] != x and i_min <= i_max:  # i_min toujours inférieur ou égal à i_max, sinon incohérence
        if x < L[i_moy]:
            i_max = i_moy - 1
        else:
            i_min = i_moy + 1

        i_moy = (i_min + i_max) // 2

    if i_min <= i_max:  # Vérifie si pas d'incoréhence
        return True, i_moy

    elif i_moy < 0:  # Cas extrème inférieur
        return False, 0
    elif i_moy >= len(L) - 1:  # Cas extrème supérieur
        return False, len(L) - 1

    # Observation : L[i_moy] < x < L[i_moy + 1]

    elif abs(L[i_moy] - x) <= abs(L[i_moy + 1] - x):  # Cas x est plus proche de L[i_moy]
        return False, i_moy
    else:  # Cas x est plus proche de L[i_moy + 1]
        return False, i_moy + 1
