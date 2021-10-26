def cherche_motif(mot: str, texte: str):
    """
    Détermine si mot est présent dans le texte

    :param str mot: Mot à chercher dans le texte
    :param str texte: Texte à analysé
    :return bool result: Si mot est présent dans texte
    """
    length_texte = len(texte)
    length_mot = len(mot)
    result = False
    i = 0

    while i <= length_texte - length_mot and not result:  # Permet de sortir de la boucle dès que le mot est trouvé
        if texte[i: i + length_mot] == mot:  # Vérifie si la chaîne de caractère de même longueur que mot est mot
            result = True

        i += 1

    return result


def cherche_motif2(mot: str, texte: str):
    """
    Retourne tous les indices des occurrences de mots dans texte

    :param str mot: Mot à trouver dans texte
    :param str texte: Texte à analyser
    :return list result: Liste des indices
    """
    length_mot = len(mot)
    result = []

    for i in range(len(texte)):
        if texte[i: i + length_mot] == mot:
            result.append(i)

    return result
