def indice_max(array: list):
    m = array[0]
    index_m = 0

    for i in range(1, len(array)):
        if array[i] > m:
            index_m = i
            m = array[i]

    return index_m


def tri_select(array: list):
    for i in range(len(array), 1, -1):
        i_max = indice_max(array[:i])
        array[i_max], array[i - 1] = array[i - 1], array[i_max]

    return array