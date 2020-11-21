from math import ceil

"""
k => n
1..9 => 1..9
10..99 => 11..189 = 9 + 2*i (i=1..90)
100..999 => 192..2890 = 189 + 3*i (i=1..900)
"""
def solve(N, K, deadline=3):
    "В условии ничего не сказано про возможные лишние цифры"
    "Так что, при некорректном N(=190, например) поведение не определено =)"

    # assert 10 < N < 1010

    pages = (99 + (N - 189) // 3) if N > 189 else (9 + (N - 9) // 2)

    return ceil(pages / (deadline*K))

assert solve(12, 1) == 4
assert solve(12, 4) == 1
assert solve(1010, 1) == 124


# N, K = map(int, input.split())

# print(solve(N, K))

