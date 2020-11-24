import time

def time_passed(func):
    def wrap(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('Время выполнения: {} секунд.'.format(end-start))
        return res
    return wrap

@time_passed
def second_task_0(n, x, y, z, w):
    solutions = []
    n1 = (n+1)**3
    for x in range(1, n + 1):
        x1 = x**3
        for y in range(x + 1, n + 1):
            y1 = y**3
            sum_xy = x1 + y1
            if sum_xy > n1:
                break
            for z in range(y + 1, n + 1):
                z1 = z**3
                sum_xyz = sum_xy + z1
                if sum_xyz > n1:
                    break
                w = int(sum_xyz ** (1 / 3)) + 1

                if sum_xyz == w**3:
                    solutions.append((x, y, z, w))
    return solutions

from math import ceil
@time_passed
def second_task(n, x, y, z, w):
    solutions = []
    cubes = [(x, x*x*x) for x in range(1, n+1)]
    m3 = cubes[-1][1]

    for x_, (x, x3) in enumerate(cubes):
        for y_, (y, y3) in enumerate(cubes[x_+1:]):
            for z_, (z, z3) in enumerate(cubes[x_+y_+1:]):
                x3y3z3 = x3+y3+z3
                w = ceil(x3y3z3 ** (1/3))
                if m3 >= x3y3z3 == w*w*w:
                    solutions.append((x, y, z, w))
    return solutions


sol = second_task_0(100, 0, 0, 0, 0)
print(len(sol))
s0 = set(sol)

sol = second_task(100, 0, 0, 0, 0)
print(len(sol))
s1 = set(sol)

for x, y, z, w in s1 - s0:
  print(x, y, z, w, w**3, w**3 == x**3+y**3+z**3)
