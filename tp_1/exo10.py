def somme_carre(a: int = 5, b: int = 100):
    """
    Calcule la somme des carrés des entiers compris dans l'interval [a; b]

    Les valeurs par défaut sont pour la première partie de la question

    :param int a: Borne Inférieure de l'interval de calcul
    :param int b: Borne Supérieure de l'interval de calcul
    :return int s: Somme des entiers de a à b
    """
    assert a <= b  # Vérifie si a est bien inférieur ou égal à b

    s = 0
    for n in range(a, b + 1):  # Calcule la somme des entiers de l'interval [a; b]
        s += n ** 2

    return s


def somme_carre_sup(a: int = 2021 * 2022):
    """
    Determine le plus petit entier n dont la somme des carrés de l'interval [0; n] est supérieure à a

    La valeur par défaut est solution à la dernière question

    :param int a: Borne entière à dépasser
    :return int n: Plus petit entier n dont la somme des entiers de l'interval [0; a] est supérieure à a
    """
    n = 0

    while somme_carre(0, n) <= a:  # Évalue la somme des entiers de l'intervale [0; n] par rapport à a, tant que cette
        n += 1                     # dernière est inférieur ou égale à a

    return n