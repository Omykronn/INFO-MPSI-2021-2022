test_simp = [1, 2, 5, 0, 0, 0]


def simp(polynom: list):
    last_not_null_i = -1

    for i in range(len(polynom)):
        if polynom[i] != 0:
            last_not_null_i = i

    return polynom[:last_not_null_i + 1]


def simp_selon_consigne(polynom: list):
    while polynom != [] and polynom[-1] == 0:
        polynom.pop()

    return polynom


"""
Terminaison : on a une boucle for

Correction : Sur le principe : on cherche l'indice du dernier coeff non-nul et on retourne le tableau jusqu'à cet indice
             En pratique, on parcours le tableau en enregistrant l'indice du dernier coeff non-nul, ce qui fonctionne 
             puisque l'on parcours le tableau en entier, puis on retourne la tableau jusqu'à cet indice inclus
             
             Dans le cas où polynom est constitué que de 0, on retourne polynom[:-1 + 1] = polynom[:0] = [] : OK
             
Complexité : Initialemment, on effectue 1 affectation
             Pendant un passage de boucle, on fait, dans le pire des cas, 1 comparaison et 1 affectation
             On passe n fois dans la boucle (n étant le nombre d'éléments de la liste)
             
             D'où C = 2n + 1
             Et donc C = O(n)
"""


def add(polynom1: list, polynom2: list):
    fst_smallest = len(polynom1) <= len(polynom2)

    if fst_smallest:
        min_deg = len(polynom1)
    else:
        min_deg = len(polynom2)

    max_deg = len(polynom2) + len(polynom1) - min_deg
    result = []

    for i in range(max_deg):
        if i < min_deg:
            result.append(polynom1[i] + polynom2[i])
        else:
            if fst_smallest:
                result.append(polynom2[i])
            else:
                result.append(polynom1[i])

    return simp(result)


def mul(polynom1: list, polynom2: list):
    deg = len(polynom2) + len(polynom1) - 1

    w_poly1, w_poly2 = [], []

    for i in range(deg):
        if i < len(polynom1):
            w_poly1.append(polynom1[i])
        else:
            w_poly1.append(0)

        if i < len(polynom2):
            w_poly2.append(polynom2[i])
        else:
            w_poly2.append(0)

    result = []

    for i in range(deg):
        result.append(0)

        for j in range(i + 1):
            result[i] += w_poly1[j] * w_poly2[i - j]

    return simp(result)


def evalpol(polynom: list, value: float):
    result = 0

    for i in range(len(polynom)):
        result += (value ** i) * polynom[i]

    return result
