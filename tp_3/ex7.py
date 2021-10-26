import numpy as np


def encadrement(M: np.ndarray, m: int):
    """
    Crée une bordure noire autour du tableau M, de largeur m

    :param np.ndarray M: Tableau Numpy à modifier
    :param int m: Épaisseur de la bordure
    :return np.ndarray: Tableau Numpy avec bordure
    """
    if type(M) is not np.ndarray:  # Vérifie si le tableau est un tableau numpy; sinon le convertit
        M = np.array(M, dtype=np.uint8)

    height, width = M.shape[0:2]  # Sélectionne seulement la hauteur et la largeur
    pixel_bord = np.array([0, 0, 0], dtype=np.uint8)  # Définition du type de pixel de la bordure

    result = np.array([[pixel_bord] * (width + m * 2)] * (height + m * 2), dtype=np.uint8)  # Tableau avec que des pixel_bord

    for i in range(height):
        for j in range(width):
            result[i + m][j + m] = M[i][j]  # Remplace par les cellules de M en gardant la bordure

    return result
