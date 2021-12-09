def fibo(n: int):
    last_terms = (0, 1)
    
    if n <= 1:
        return last_terms[n]
    else:
        for _ in range(n - 1):
            last_terms = (last_terms[1], last_terms[0] + last_terms[1])
        
        return last_terms[1]

def fibo_rec(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_rec(n - 1) + fibo_rec(n - 2)
