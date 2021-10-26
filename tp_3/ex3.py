def damier_couleur(n: int):
    """
    Retourne un damier carré de dimension n et d'alternance de (255, 0, 0) et de (0, 0, 255); peut être interprété comme
    un damier d'alternance rouge et bleu

    :param int n: Dimension du damier
    :return list: Damier carré de dimension n
    """
    return [[(255, 0, 0) if (i + j) % 2 == 0 else (0, 0, 255) for j in range(n)] for i in range(n)]
