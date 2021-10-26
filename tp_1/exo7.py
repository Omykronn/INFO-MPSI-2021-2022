def bissextile(annee: int):
    """
    Détermine si l'année entrée est bissextile

    :param int annee: Année à étudiée
    :return bool: Booléen correspondant si l'année est bissextile ou non
    """
    return (annee % 4 == 0 and annee % 100 > 0) or annee % 400 == 0
