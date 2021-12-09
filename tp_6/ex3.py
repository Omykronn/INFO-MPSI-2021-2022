def PGCD(a: int, b: int):  
    m = 1
    
    if b > a:
        a, b = b, a  # On veut a <= b
    
    for n in range(1, a + 1):
        if a % n == 0 and a % n == b % n:
            m = n      
                
    return m

def PGCD_rec(a: int, b: int):
    assert a >= b
    
    if b == 0:
        return a
    else:
        return PGCD_rec(a, a % b)
