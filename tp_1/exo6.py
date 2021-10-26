def fahrenheit(value: int):
    """
    Convertit une température en degré Celsius en degré Fahrenheit

    :param int value: Temperature en Fahrenheit
    :return int: Temperature en Celsius
    """
    return 9/5 * value + 32


def celsius(value: int):
    """
    Convertit une température en degré Fahrenheit en degré Celsius

    :param int value: Celsius Temperature
    :return int: Fahrenheit Temperature
    """
    return 5/9 * (value - 32)
