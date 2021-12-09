def fact(n: int):
    f = 1
    
    for x in range(n):
        f *= x + 1
    
    return f

def fact_rec(n: int):
    if n == 0:
        return 1
    else:
        return n * fact_rec(n - 1)
        