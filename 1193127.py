import math

phi = (1 + math.sqrt(5)) / 2
def fib(number): 
    fn=0
    fn = (1 / math.sqrt(5)) * (phi**number - (math.cos(math.pi * number)) / phi**number)
    return math.trunc(fn)
def orig(N):

    currentFib = 0
    i=1
    sum=0

    while True:
        currentFib = fib(i*3)
        i+=1
        if currentFib > 4e6:
            break
        sum+=currentFib
    print(sum)
    return sum


def solve(N):
    even, next_ = 0, 1
    sum_ = 0

    while even <= N:
        sum_ += even
        next_, even = (
            3 * next_ + 2 * even,
            2 * next_ + even,
        )

    return sum_

def solve2(N):
    a, b = 0, 2
    sum_ = 0 
    while b <= N:
        sum_ += b
        a, b = b, a+4*b

    return sum_

def solveC(N):
    sqrt5 = math.sqrt(5)
    phip = (1 + sqrt5) / 2
    phim = (1 - sqrt5) / 2
    def sumFirstEvenFib(n):
        res = phip ** 3 * (phip ** (3*n) - 1) / (phip ** 3 - 1) \
            - phim ** 3 * (phim ** (3*n) - 1) / (phim ** 3 - 1)
        
        res /= sqrt5

        return math.floor(res)
    assert sumFirstEvenFib(0) == 0
    assert sumFirstEvenFib(1) == 2
    assert sumFirstEvenFib(2) == 10
    n = round(math.log(N*sqrt5, phip), 2) // 3

    return sumFirstEvenFib(n)

def sum_phib_even(N):
  from math import sqrt, log, trunc
  'Fat-Zer'
  if (N<8): 
    return 2 
  phi = (1 + sqrt(5)) / 2

  n = trunc( log(N*sqrt(5), phi) )
  if (n%3 == 2 and fib(n+1) <= N):
  # if (n%3 == 2):
    n = n+1
  n //= 3

  return (fib(n*3+2) - 1) / 2

assert orig(4e6) == 4613732
assert solve(4e6) == 4613732
assert solve2(4e6) == 4613732
assert sum_phib_even(4e6) == 4613732
assert solve2(50) == 44
assert sum_phib_even(2) == 2
assert sum_phib_even(7) == 2
print(sum_phib_even(143))
assert sum_phib_even(143) == 44, '188==44'
assert solveC(2) == 2
assert solveC(7) == 2
# assert solveC(8) == 10
assert solveC(143) == 44
assert solveC(144) == 188
assert solveC(4e6) == 4613732
print(2**50)
print(solve2(2.2e15))
print(sum_phib_even(2.2e15))

cur, prev = 0, 0
# for i in range(2, 14930352+1):
# for i in range(14930352, 63245986+1):
#     cur= sum_phib_even(i)
#     if cur != prev:
#         print(i, cur)
#         prev = cur


sqrt5 = math.sqrt(5)
A014445 = [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578, 14930352, 63245986, 267914296, 1134903170, 4807526976, 20365011074, 86267571272, 365435296162, 1548008755920, 6557470319842, 27777890035288, 117669030460994, 0,0,0]
for i in range(len(A014445)):
    x = A014445[i]
    k = log10(5)/2 + log10(x)
    print(i, k, A014445[i])
    assert math.floor(k) == A014445[i] or not A014445[i]

# for x in A014445:
#     'k * sqrt5 = (2+sqrt5)**i - (2-sqrt5)**i'
#     pass


"""
2 2
5 10
22 44
89 188
378 798
1597 3382
6766 14328
28657 60696
121394 257114
514229 1089154
2178310 4613732
9227465 19544084
"""
