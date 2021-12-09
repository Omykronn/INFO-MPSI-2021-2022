def dicho(f, a: float, b: float, eps: float):
    assert a < b
    
    m = (a + b) / 2
    
    while abs(f(m)) > eps:
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
            
        m = (a + b) / 2
        
    return m

def dicho_rec(f, a: float, b: float, eps: float):
    assert a < b
    
    m = (a + b) / 2
    
    if abs(f(m)) <= eps:
        return m
    elif f(m) * f(a) <= 0:
        return dicho_rec(f, a, m, eps)
    else:
        return dicho_rec(f, m, b, eps)
