def damier(n: int):
    """
    Retourne un damier carré d'alternance de 0 et de 1

    :param int n: Dimension du damier à retourner
    :return list: Damier carré de dimension n
    """
    return [[(i + j) % 2 for j in range(n)] for i in range(n)]
