import numpy as np


def noir_et_blanc(array: np.ndarray):
    """
    Crée un rendu de l'image associée au tableau array en noir et blanc à l'aide de la moyenne des composantes
    trichromatiques

    :param np.ndarray array: Tableau associée à une image
    :return np.ndarray: Tableau associée à l'image transformée en noir et blanc
    """
    def average(data: list):
        """
        Calcule la moyenne des valeurs contenues dans data

        :param list data: Liste des valeurs
        :return int: Moyenne des valeurs
        """
        s = 0

        for n in data:
            s += n

        return s / len(data)

    height, width, dimension = array.shape

    for i in range(height):
        for j in range(width):
            array[i][j] = np.array(int(average(array[i][j][:3])))

    return array


def noir_et_blanc2(array: np.ndarray):
    """
    Crée un rendu de l'image associée au tableau array en noir et blanc à l'aide d'une formule sur les composantes
    trichromatiques

    :param np.ndarray array: Tableau associée à une image
    :return np.ndarray: Tableau associée à l'image transformée en noir et blanc
    """
    height, width, dimension = array.shape

    for i in range(height):
        for j in range(width):
            array[i][j] = np.array(int(array[i][j][0] * 0.299 + array[i][j][1] * 0.587 + array[i][j][2] * 0.114))

    return array