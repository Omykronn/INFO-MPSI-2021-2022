import numpy as np


def miroir_horizontal(M: np.ndarray):
    """
    Effectue une symétrie horizontale du tableau M

    :param np.ndarray M: Tableau Numpy à modifier
    :return np.ndarray: Tableau Numpy horizontalement symétrique à M
    """
    if type(M) is not np.ndarray:  # Vérifie si le tableau est un tableau numpy; sinon le convertit
        M = np.array(M, dtype=np.uint8)

    height, width = M.shape[0:2]  # Sélectionne seulement la hauteur et la largeur

    return np.array([[M[i][j] for j in range(width)] for i in range(height - 1, -1, -1)], dtype=np.uint8)
