def primality(p):
    polynomial = np.poly1d(np.array([1,-1], dtype=object)) ** p
    coefficients = polynomial.c
    coefficients = (list(coefficients).pop(0).pop(-1))
    prime = all(c % p == 0 for c in coefficients)
    return prime
