test = [0, 0, 1, 0, 0, 0]


def nombreZeroDroite(i, tab, n):
    nb = 0

    while i + nb < n and tab[i + nb] == 0:
        nb += 1

    return nb


def nombreZerosMaximum(tab, n):
    max_0 = 0
    i = 0
    
    while i < n:
        temp = nombreZeroDroite(i, tab, n)

        if temp > max_0:
            max_0 = temp

        if temp == 0:
            i += 1
        else:
            i += temp

    return max_0


test2 = [[0, 0, 1, 1, 0, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0, 0, 0, 1],
         [0, 0, 1, 1, 0, 0, 0, 1],
         [0, 0, 1, 0, 0, 0, 0, 1],
         [0, 1, 1, 1, 0, 1, 0, 1],
         [0, 0, 1, 1, 0, 0, 0, 1]]


def rectangleHautDroit(tab2, n, i, j):
    j_incr = nombreZeroDroite(j, tab2[i], n)
    area_max = j_incr
    i_incr = 1

    while i - i_incr >= 0 and j_incr > 0:
        j_temp = nombreZeroDroite(j, tab2[i - i_incr], n)

        if j_temp < j_incr:
            j_incr = j_temp

        i_incr += 1
        area_temp = j_incr * i_incr  # Attention la valeur de i_incr a été incrémentée de 1 par rapport au calcul précédent

        if area_temp > area_max:
            area_max = area_temp
        
    return area_max


def colonneZeros(tab2, n):
    col = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for i in range(n):            
            if tab2[i][j] == 0:
                if i == 0:  # Si Case la plus haute case : donc forcement 1
                    col[i][j] = 1
                else:  # Si pas la case la plus haute : +1 de la précédente
                    col[i][j] = col[i - 1][j] + 1
            else:
                col[i][j] = 0

    return col
                
        
        
