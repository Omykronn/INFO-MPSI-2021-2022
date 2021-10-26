from PIL import Image
import numpy as np


def import_image_as_array(dir: str, numpy_format: bool = True):
    """
    Importe une image sous forme d'un tableau

    :param str dir: Directory du fichier image
    :param bool numpy_format: Booléen sur le format de sortie : si True, format numpy, sinon; format list
    :return: Tableau de l'image
    """
    array = Image.open(dir).copy()

    if dir[-3:] == "png":  # Avertit l'User sur le png, format avec une quatrième variable de transparence
        raise Warning("Une Image PNG fonctionne de manière légérement différente, ce qui peut engendrer des erreurs")

    if numpy_format:
        array = np.array(array, dtype=np.uint8)

    return array


def export_array_as_image(array: list, dir: str):
    """
    Exporte un tableau sous forme d'image

    :param array: Tableau à convertir
    :param dir: Directory du fichier de sortie
    :return: None
    """
    if type(array) is not np.ndarray:  # Vérifie si le tableau est un tableau numpy, sinon le convertit
        array = np.array(array, dtype=np.uint8)

    if dir[-3:] == "png":  # Avertit l'User sur le png, format avec une quatrième variable de transparence
        raise Warning("Une Image PNG fonctionne de manière légérement différente, ce qui peut engendrer des erreurs")

    Image.fromarray(array).save(dir)
    print("DONE")
