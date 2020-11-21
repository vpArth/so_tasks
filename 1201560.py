def foo(n, k):
    if k == n or k == 0:
        return 1

    return n * foo(n - 1, k-1) // k


def calc(n, k):
    if k == 0:
        return 1

    return calc(n, k - 1) * (n - k + 1) // k

from itertools import combinations
N = 10
pad = 8
for k in range(N):
    for n in range(k, N):
        Cnk = foo(n, k)
        # assert Cnk == len([*combinations(range(n), k)])

        print(f'{Cnk:{pad}}', end=' ')

    print()


assert foo(10, 1) == len([*combinations(range(10), 1)])
assert foo(10, 2) == len([*combinations(range(10), 2)])
assert foo(10, 10) == len([*combinations(range(10), 10)])
assert foo(20, 10) == len([*combinations(range(20), 10)])
