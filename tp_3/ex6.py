import numpy as np


def rotation(array: np.ndarray):
    """
    Retourne un tableau de l'image originale (contenue dans le tableau array) tournée de 90° (sens horaire)

    :param np.ndarray array: Tableau associée à l'image originale associée
    :return np.ndarray: Tableau associée à l'image tournée
    """
    height, width = array.shape[:2]

    empty_pixel = np.array([0, 0, 0], dtype=np.uint8)  # Pixel type sans importance (juste pour le bon typage)
    result = np.array([[empty_pixel] * height] * width, dtype=np.uint8)  # Tableau rempli de empty_pixel

    for i in range(height):
        for j in range(width):
            result[j][height - i - 1] = array[i][j]

    return result
