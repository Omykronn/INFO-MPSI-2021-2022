def fusion(array1: list, array2: list):
    result = []

    a, b = 0, 0
    a_max, b_max = len(array1), len(array2)

    while a < a_max and b < b_max:
        if array1[a] < array2[b]:
            result.append(array1[a])
            a += 1
        else:
            result.append(array2[b])
            b += 1

    if a < a_max:
        result += array1[a:]
    elif b < b_max:
        result += array2[b:]

    return result


def tri_fusion(array: list):
    if len(array) == 1:
        return array
    else:
        i_sep = len(array) // 2
        return fusion(tri_fusion(array[:i_sep]), tri_fusion(array[i_sep:]))