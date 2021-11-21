def tri_bulle(array: list):
    changed = True

    while changed:
        changed = False

        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                changed = True

    return array