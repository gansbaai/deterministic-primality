def primality(p):
    polynomial = np.poly1d(np.array([1,-1], dtype=object)) ** p
    coefficients = (list(polynomial.c).pop(0).pop(-1))
    prime = all(c % p == 0 for c in coefficients)
    return prime
