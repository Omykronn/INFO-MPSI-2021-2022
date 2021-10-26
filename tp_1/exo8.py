def compare(value1: float, value2: float):
    """
    Retourne la plus grande valeur entre value1 et value2

    :param float value1: Premier nombre à comparer
    :param float value2: Deuxième nombre à comparer
    :return float: Maximum entre value1 et value2
    """
    return value1 if value1 >= value2 else value2


def compare_pair(pair: list):
    """
    Retourne le maximum des valeurs de la paire donnée

    :param list pair: Paire à étudier
    :return float: Élement maximum de la paire
    """
    assert len(pair) == 2  # Vérifie si le tableau est bien une paire

    return pair[0] if pair[0] >= pair[1] else pair[1]
