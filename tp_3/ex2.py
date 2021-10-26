def damier(n: int):
    """
    Retourne un damier carré de dimension n et d'alternance de 0 et de 255 : peut être interprété comme un damier
    d'alternance noir et blanc

    :param int n: Dimension du damier
    :return list: Damier carré de dimension n
    """
    return [[255 * ((i + j) % 2) for j in range(n)] for i in range(n)]
