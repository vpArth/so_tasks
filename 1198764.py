from math import sqrt
from decimal import Decimal

def confract(num):
    den = 1
    a, q = divmod(num, den)
    t = den
    res = [a]
    while q != 0:
        next_t = q
        a, q = divmod(t, q)
        t = next_t
        res.append(a)
    return res

m = Decimal(21299881)
print(m.sqrt(), sqrt(21299881), *confract(m.sqrt()))

