import numpy as np


def agrandissement(M: np.ndarray, m: int):
    """
    Renvoie un tableau m-fois plus grand que l'original M

    :param np.ndarray M: Tableau Numpy Original
    :param int m: Facteur d'agrandissement
    :return np.ndarray: Tableau numpy agrandi
    """
    if type(M) is not np.ndarray:  # Vérifie si le tableau est un tableau numpy; sinon le convertit
        M = np.array(M, dtype=np.uint8)

    height, width = M.shape[0:2]  # Sélectionne seulement la hauteur et la largeur
    empty_pixel = np.array([0, 0, 0], dtype=np.uint8)  # Définition du type de pixel de la bordure

    result = np.array([[empty_pixel] * (width * m)] * (height * m), dtype=np.uint8)  # Tableau m-fois plus grand et avec
                                                                                     # que des empty_pixel
    for i in range(m * height):
        for j in range(m * width):
            result[i][j] = M[i // m][j // m]

    return result
