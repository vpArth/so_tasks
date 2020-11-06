from itertools import permutations
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sqr_dist(self, other):
        "Квадрат расстояния - этого достаточно, чтобы отличать разные расстояния между точками"
        return (self.x - other.x)**2 + (self.y - other.y)**2;
    def __repr__(self):
        return f'<Point {self.x}, {self.y}>'

n = int(input())
# Считываем все точки в массив
a = []
for i in range(n):
    a.append(Point(*[int(x) for x in input().split()]))

# Найденные расстояния складываем в множество, дубликаты отбрасываются автоматически
unique_dists = set()
# Генерируем все комбинации пар точек
for (a, b) in permutations(a, 2):
    # Считаем растояния между точками пары
    unique_dists.add(a.sqr_dist(b))

dists = sorted([round(sqrt(sqr_dist), 9) for sqr_dist in unique_dists])
print(len(dists))
for dist in dists:
    print(dist)
