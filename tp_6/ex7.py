def A(m: int, n: int):
    assert m >= 0 and n >= 0
    
    if m == 0:
        return n + 1
    elif n == 0:
        return A(m - 1, 1)
    else:
        return A(m - 1, A(m, n - 1))
