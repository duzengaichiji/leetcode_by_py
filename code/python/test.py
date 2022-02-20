def gcd(a, b):
    if a == b:
        return a
    if a < b:
        if b % a == 0:
            return a
        return gcd(a, b % a)
    return gcd(b, a)