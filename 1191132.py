import time
def time_passed(func):
    def wrap(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('Время выполнения: {} секунд.'.format(end-start))
        return res

    return wrap

from math import ceil

@time_passed
def second_task0(n, x, y, z, w):
    solutions = []
    cubes = [x*x*x for x in range(1, n+1)]
    cube_set = set(cubes)

    for x_, x3 in enumerate(cubes):
        x = x_ + 1
        for y_, y3 in enumerate(cubes[x_+1:]):
            y = x + y_ + 1
            for z_, z3 in enumerate(cubes[x_+y_+2:]):
                z = y + z_ + 1
                x3y3z3 = x3+y3+z3
                if x3y3z3 in cube_set:
                    w = ceil(x3y3z3 ** (1/3))
                    solutions.append((x, y, z, w))
    return solutions

@time_passed
def second_task(n, x, y, z, w):
    solutions = []
    cubes = [(x, x*x*x) for x in range(1, n+1)]
    m3 = cubes[-1][1]

    for x, x3 in cubes:
        for y, y3 in cubes[x:]:
            for z, z3 in cubes[y:]:
                x3y3z3 = x3+y3+z3
                w = ceil(x3y3z3 ** (1/3))
                if m3 >= x3y3z3 == cubes[w-1][1]:
                    solutions.append((x, y, z, w))

    return solutions

sol = second_task0(1000, 0, 0, 0, 0)
print(len(sol), sol)

sol = second_task(1000, 0, 0, 0, 0)
print(len(sol), sol)
