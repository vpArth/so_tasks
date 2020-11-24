from collections import Counter


def input_words():
    n = int(input())
    for _ in range(n):
        yield input()

def solve(word_iter):
    uniqueness = set()
    counter = Counter()
    for word in word_iter:
        if word not in uniqueness: # Не рассматриваем дубликаты
            uniqueness.add(word)
            key = ''.join(sorted(word))
            counter[key] += 1
    result = 0
    for key in counter:
        r = counter[key]
        # Кол-во сочетаний = r! / 2 (r-2)!
        result += r*(r-1)//2

    return result
# cnt = solve(input_words())
cnt = solve([
    'qwertyuiop',
    'twoplussix',
    'poiuytrewq',
    'plustwosix',
    'poiuqwerty',
    'poiuqwerty', # duplicate
])

print(cnt) # 4
