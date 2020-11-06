def solve(n):
    if (n & 1) == 0:
        return n >> 1
    i = 3

    while i*i <= n:
        if n % i == 0:
            return n // i
        i += 2;

    return 1



print(solve(118051))
print(solve(118051*11))
print(solve(118051*118051))
print(solve((1 << 64) - 1))
print(solve(18446744065119617025));
# print(solve(18446744073709551557)); # max 64-bit prime, 7 minutes
