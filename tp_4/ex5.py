def zerof(func, a, b, eps):
    """
    Trouve une valeur d'annualation approchée de la fonction f sur l'interval [a; b] avec une précision de eps

    :param func: Fonction à étudiée
    :param a: Borne inférieure de l'interval d'étude
    :param b: Borne supérieure de l'interval d'étude
    :param eps: Précision du résultat
    :return float: Approximation de la Valeur d'annulation (± eps) de f sur [a; b]
    """
    x = (a + b) / 2

    while abs(func(a) - func(b)) > eps:
        if func(a) * func(x) < 0:
            b = x
        else:
            a = x

        x = (a + b) / 2

    return x


def f(x):
    """
    Fonction trouvée dans l'annexe de chimie, pour déterminer la valeur de l'avancement finale

    :param float x: Valeur à calculer
    :return float: Image de x par f
    """
    return -2300 * x**5 + 4600 * x**4 - 3168 * x**3 + 1008 * x**2 - 153 * x + 9


print(zerof(f, 0, 0.25, 1e-15))

""" 
Réponse : ξ_F = 0.20000000000001616 ± 10^-15 mol (en vrai, c'est 0.2 mol)

NB: À partir de 10^-15, l'affichage de Python n'est pas suffisament précis
"""
