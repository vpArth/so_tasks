from math import sqrt

def sqrt_frac(c):
    res = []
    i = 0


    p = 1
    while p*p < c:
        p += 1
    p -= 1
    res.append(p)

    rest = c - p*p;

    a = int(2*p/rest);
    res.append(a)

    print('rest', rest)

    # x*x = c
    # x*x - p*p = c - p*p
    # x = p + 1 / (2*p/(c-p*p) + 1/(2*p + x-p))

    return res

# print(sqrt_frac(17))
print(sqrt_frac(21299881)) # 4615 5 1 1 2 1 7 1 27 1 6 1 2 12 23 1 8 2 3 6 1 1 1 4 1 7 1 1 1 43 3 4 2 1 1 11 1 7 1 4 5 2 2 4 4 4

"""
4615 + 1
       5 + 1
           1 + 1
               1 + 1
                   2 + 1
                       1 + 1
                           7 + 1
                               1 + 1
                                   27


"""
