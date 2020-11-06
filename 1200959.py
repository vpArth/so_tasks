from timeit import timeit

print(timeit('x = 1212345678901234567890; int(x)', number=int(1e8)))
print(timeit('x = 1212345678901234567890; int(x) if type(x) is not int else x', number=int(1e8)))

"""
5.075638975016773
6.453564461087808
"""
