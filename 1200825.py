"""
Дано натуральное число n.
Найдите количество упорядоченных пар натуральных чисел (i, j) таких, что i*j=n,
и наибольший общий делитель чисел i и j равен 1
"""

from math import sqrt, gcd;

DEBUG = True
def solve(n):
    p = print if DEBUG else lambda *args, **kwargs:None;

    p(f'solve({n})')
    k = 0
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            j = n // i

            if gcd(i, j) == 1:
                p(f'{i:3} * {j:6}', end='; ')
                k += 1
            if k % 10 == 0:
                p()
    p(f'\nresult is {k}\n')
    return k

assert solve(12) == 2 # 1*12, 3*4
assert solve(30030) == 32
assert solve(510510) == 64
