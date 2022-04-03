test = [i for i in range(10)]


def moycroiss(u: list):
    n_max = len(u) - 3
    state = True
    i = 0

    while i < n_max and state:
        state = u[i] + u[i + 1] + u[i + 2] <= u[i + 1] + u[i + 2] + u[i + 3]
        i += 1

    return state

"""
Terminaison : à chaque entrée de boucle, i a été incrémentée de 1 et n_max est une valeur fixée : la terminaison est
              ainsi assurée
              
Correction : A chaque passage de boucle, on vérifie l'assertion, et donc pour tous les indices nécessaires, et chaque
             entrée dans la boucle, on vérifie si l'assertion précédente était juste, si elle l'était : on continue,
             sinon on arrête la boucle et on renvoi False (cohérent)
             Dans le cas ou l'assertion est vérifiée par tous les indices, on renvoit True
             
Complexité : Initialement, on a effectué 3 affectations et 1 opération
             A chaque passage de boucle, on effectue 5 additions, 3 comparaisons 
             
             Dans le pire des cas, on effectue n - 3 passages, d'où C = (n - 3)(5 + 3) + 4 = 8n - 20
             Donc C = O(n)
"""
