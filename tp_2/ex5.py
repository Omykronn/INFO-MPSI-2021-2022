def doublon(L: list):
    """
    Retourne une valeur contenue dans la liste L qui apparait deux fois ou plus

    :param list L: Liste à analysée
    :return int: Valeur de la liste L dont l'occurrence est supérieur ou égale à 2
    """
    occurrence = {}  # Dictionnnaire renseignant l'occurrence de chaque valeur de la liste L

    for element in L:  # Compte les occurrences de chaque valeur
        if element in occurrence:  # Vérifie si element est déjà renseigné dans le dictionnaire occurrence
            occurrence[element] += 1
        else:
            occurrence[element] = 1

    value = None

    for item in occurrence:  # Determine un element de occurrence dont l'occurrence est supérieure ou égale à 2
        if occurrence[item] >= 2:
            value = item

    return value


def doublon_liste(L: list):
    """
        Retourne la liste des valeurs contenues dans la liste L qui apparaissent deux fois ou plus

        :param list L: Liste à analysée
        :return list: Liste des Valeurs de la liste L dont l'occurrence est supérieur ou égale à 2
        """
    occurrence = {}  # Dictionnnaire renseignant l'occurrence de chaque valeur de la liste L

    for element in L:  # Compte les occurrences de chaque valeur
        if element in occurrence:  # Vérifie si element est déjà renseigné dans le dictionnaire occurrence
            occurrence[element] += 1
        else:
            occurrence[element] = 1

    array = []

    for item in occurrence:
        if occurrence[item] >= 2:
            array.append(item)

    return array


def proches(L: list):
    """
    Détermine un couple d'élements à distance est minimale

    :param L: Liste à étudiée
    :return tuple element: Couple avec deux éléments à distance minimale
    """

    def difference_abs(item1: float, item2: float):
        """
        Renvoie la valeur absolue de la différence de item1 et item2

        :param float item1: Valeur 1
        :param float item2: Valeur 2
        :return float: Valeur absolue de la différence de item1 et item2
        """
        if item1 >= item2:
            return item1 - item2
        else:
            return item2 - item1

    length = len(L)
    element = None
    distance = None

    for i in range(length):
        for j in range(i + 1, length):
            if distance is None or difference_abs(L[i], L[j]) < distance:
                element = (L[i], L[j])
                distance = difference_abs(L[i], L[j])

    return element


def proches2(L: list):
    """
    Retourne l'ensemble des couples d'élements à distance minimale

    :param list L: Liste à analysée
    :return list array: Ensemble des couples
    """

    def difference_abs(item1: float, item2: float):
        """
        Renvoie la valeur absolue de la différence de item1 et item2

        :param float item1: Valeur 1
        :param float item2: Valeur 2
        :return float: Valeur absolue de la différence de item1 et item2
        """
        if item1 >= item2:
            return item1 - item2
        else:
            return item2 - item1

    length = len(L)
    array = []
    distance = None

    for i in range(length):
        for j in range(i + 1, length):
            if distance is None or difference_abs(L[i], L[j]) < distance:
                array = [(L[i], L[j])]
                distance = difference_abs(L[i], L[j])
            elif difference_abs(L[i], L[j]) == distance:
                array.append((L[i], L[j]))

    return array
