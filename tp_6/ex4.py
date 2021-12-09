def palindrome(s: str):
    m = len(s) // 2
    i = 0
    
    state = True
    
    while state and i <= m:
        state = s[i] == s[-(i + 1)]
        i += 1
    
    return state

def palindrome_rec(s: str):
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return palindrome_rec(s[1:-1])
    else:
        return False
