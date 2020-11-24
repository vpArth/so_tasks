import numpy as np

def copy(p):
    return np.array(p)

align_divmul = [0, 0, 0, 3, 3, 3, 6, 6, 6];

def row(p, n):
    return p[n]
def col(p, n):
    return p[:, n]
def sqr(p, *args):
    if len(args) == 1:
        row, col = align_divmul[args[0]], args[0] % 3 * 3
    else:
        row, col = align_divmul[args[0]], align_divmul[args[1]]

    return p[row:row+3, col:col+3]



full = (1 << 10) - 2
def bitset(l):
    r = 0
    for x in l:
        r |= 1 << x
    return r

def bitset_first(bs):
    if bs == 0:
        return 0
    x = 0
    while bs:
        if bs&1:
            return x
        x += 1
        bs >>= 1

def bitset_iter(bs):
    x = 0
    while bs:
        if bs&1:
            yield x
        x += 1
        bs >>= 1

def candidates_for(p):
    rows = [full] * 9
    cols = [full] * 9
    sqrs = [full] * 9

    for i in range(9):
        for j in range(9):
            if p[i][j] != 0:
                d = p[i][j]
                x = ~(1 << d)
                rows[i] &= x
                cols[j] &= x
                sqrs[align_divmul[i]+j//3] &= x
    return [[
        rows[i] & cols[j] & sqrs[align_divmul[i]+j//3] if p[i][j] == 0 else 1 << p[i][j]
        for j in range(9)
    ] for i in range(9)]

def is_bad(p, C = None):
    for i in range(9):
        if C:
            for j in range(9):
                if C[i][j] == 0:
                    return True


        row = p[i]
        col = p[:,i]
        idiv3, imod3 = align_divmul[i], i%3*3
        sqr = p[i//3*3:i//3*3+3, i%3*3:i%3*3+3].flatten()


        for part in row, col, sqr:
            if not (np.unique(part[part>0], return_counts=True)[1] == 1).all():
                return True

    return False

def has_zeroes(p):
    return 0 in p

def is_solved(p):
    if is_bad(p):
        return False

    return not has_zeroes(p)

def print_p(p):
    print('-'*9*3, *(p if p is not None else [p]), sep='\n')

def print_c(C):
    print('-'*9*3, *[[list(bitset_iter(bs)) for bs in r] for r in C], sep='\n')

def exclude(C, i, j, d):
    xi = align_divmul[i] # i // 3 * 3
    xj = align_divmul[j] # j // 3 * 3
    x = ~(1<<d)
    for t in range(9):
        if t != j:
            C[i][t] &= x
        if t != i:
            C[t][j] &= x
        si, sj = xi+t//3, xj+t%3
        if si != i or sj != j:
            C[si][sj] &= x

def c_has_alt(C, i, j, d):
    xi = align_divmul[i] # i // 3 * 3
    xj = align_divmul[j] # j // 3 * 3
    x = 1 << d
    for t in range(9):
        if t != j and (C[i][t] & x):
            return True
        if t != i and (C[t][j] & x):
            return True
        si, sj = xi+t//3, xj+t%3
        if si != i or sj != j:
            if C[si][sj] & x:
                return True

    return False



def resolve(p, C = None):
    C = candidates_for(p) if C is None else C

    changing = True
    while changing:
        changing = False
        for i in range(9):
            for j in range(9):
                # Find only candidates
                if p[i][j] == 0:
                    x = C[i][j]
                    if x and x&(x-1) == 0:
                        d = bitset_first(x)

                        p[i][j] = d

                        changing = True
                        exclude(C, i, j, d)

                    # else:
                        # Find except candidates
                        # for d in bitset_iter(C[i][j]):
                        #     if not c_has_alt(C, i, j, d):
                        #         p[i][j] = d
                        #         C[i][j] = 1 << d
                        #         changing = True

def sudoku_solver(puzzle):
    result = solve(puzzle)
    if result is None:
        raise Exception('Unsolvable one')
    return result

def solve(puzzle):
    if puzzle is None:
        return None

    solution = copy(puzzle)

    if is_bad(solution):
        return None

    C = candidates_for(solution)
    resolve(solution, C)

    if is_bad(solution, C):
        return None

    if not has_zeroes(solution):
        return solution

    for i in range(9):
        for j in range(9):
            if solution[i][j] == 0:
                for d in bitset_iter(C[i][j]):
                # for d in range(1, 10):
                    solution[i][j] = d
                    res = solve(solution)
                    if res is not None:
                        return res


# ###############

wrong_1 = [[0, 9, 6, 5, 0, 4, 0, 7, 1], [0, 2, 0, 1, 0, 0, 0, 0, 0], [0, 1, 4, 0, 9, 0, 6, 2, 3], [0, 0, 3, 0, 6, 0, 0, 8, 0], [0, 0, 8, 0, 5, 0, 4, 0, 0], [9, 0, 0, 4, 1, 0, 0, 0, 5], [7, 0, 0, 0, 0, 9, 0, 0, 0], [0, 0, 1, 0, 7, 5, 3, 4, 9], [2, 3, 0, 0, 4, 8, 1, 0, 7]]
ok_1 = [[0, 0, 0, 0, 0, 2, 7, 5, 0], [0, 1, 8, 0, 9, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 9, 0, 0, 0, 0, 0, 0, 0], [0, 3, 0, 0, 0, 0, 0, 0, 8], [0, 0, 0, 7, 0, 0, 2, 0, 0], [0, 0, 0, 0, 3, 0, 0, 0, 9], [7, 0, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 0, 0, 0, 0, 8, 0]]
ok_2 = [[8, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 6, 0, 0, 0, 0, 0], [0, 7, 0, 0, 9, 0, 2, 0, 0], [0, 5, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 4, 5, 7, 0, 0], [0, 0, 0, 1, 0, 0, 0, 3, 0], [0, 0, 1, 0, 0, 0, 0, 6, 8], [0, 0, 8, 5, 0, 0, 0, 1, 0], [0, 9, 0, 0, 0, 0, 4, 0, 0]]
ok_3 = [[0, 9, 0, 0, 7, 1, 0, 0, 4], [2, 0, 0, 0, 0, 0, 0, 7, 0], [0, 0, 3, 0, 0, 0, 2, 0, 0], [0, 0, 0, 9, 0, 0, 0, 3, 5], [0, 0, 0, 0, 1, 0, 0, 8, 0], [7, 0, 0, 0, 0, 8, 4, 0, 0], [0, 0, 9, 0, 0, 6, 0, 0, 0], [0, 1, 7, 8, 0, 0, 0, 0, 0], [6, 0, 0, 0, 2, 0, 7, 0, 0]]

def match(p, X):
    for i in range(9):
        for j in range(9):
            if 0 != p[i][j] != X[i][j]:
                return False
    return True


def test_solve(x):
    result = solve(x)
    print_p(result)
    print(result is not None and is_solved(result))

def test_1():
    puzzle = [[0, 0, 6, 1, 0, 0, 0, 0, 8],
              [0, 8, 0, 0, 9, 0, 0, 3, 0],
              [2, 0, 0, 0, 0, 5, 4, 0, 0],
              [4, 0, 0, 0, 0, 1, 8, 0, 0],
              [0, 3, 0, 0, 7, 0, 0, 4, 0],
              [0, 0, 7, 9, 0, 0, 0, 0, 3],
              [0, 0, 8, 4, 0, 0, 0, 0, 6],
              [0, 2, 0, 0, 5, 0, 0, 8, 0],
              [1, 0, 0, 0, 0, 2, 5, 0, 0]]

    solution = [[3, 4, 6, 1, 2, 7, 9, 5, 8],
                [7, 8, 5, 6, 9, 4, 1, 3, 2],
                [2, 1, 9, 3, 8, 5, 4, 6, 7],
                [4, 6, 2, 5, 3, 1, 8, 7, 9],
                [9, 3, 1, 2, 7, 8, 6, 4, 5],
                [8, 5, 7, 9, 4, 6, 2, 1, 3],
                [5, 9, 8, 4, 1, 3, 7, 2, 6],
                [6, 2, 4, 7, 5, 9, 3, 8, 1],
                [1, 7, 3, 8, 6, 2, 5, 9, 4]]

    actual = solve(puzzle)
    print_p(actual)
    print(actual and is_solved(actual), actual == solution)

def test_2():
    puzzle = [
        [1, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 2, 6, 0, 0, 0, 0, 3, 0],
        [0, 8, 0, 0, 0, 4, 0, 0, 1],
        [2, 0, 0, 0, 0, 8, 9, 0, 0],
        [0, 9, 0, 4, 0, 7, 0, 1, 6],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 3],
        [4, 1, 0, 0, 0, 2, 0, 0, 8],
        [8, 7, 0, 0, 0, 0, 0, 0, 0]]

    solution = [
        [1, 3, 4, 8, 9, 6, 2, 5, 7],
        [9, 2, 6, 1, 7, 5, 8, 3, 4],
        [7, 8, 5, 2, 3, 4, 6, 9, 1],
        [2, 6, 7, 3, 1, 8, 9, 4, 5],
        [5, 9, 8, 4, 2, 7, 3, 1, 6],
        [3, 4, 1, 6, 5, 9, 7, 8, 2],
        [6, 5, 9, 7, 8, 1, 4, 2, 3],
        [4, 1, 3, 9, 6, 2, 5, 7, 8],
        [8, 7, 2, 5, 4, 3, 1, 6, 9],
    ]

    actual = solve(puzzle)
    print_p(actual)
    print(actual and is_solved(actual), actual == solution)

def test_3():
    puzzle = [
        [4, 0, 0, 0, 2, 0, 8, 1, 7],
        [7, 1, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 6],
        [0, 4, 0, 2, 0, 0, 9, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 1, 0, 6, 0, 0, 7, 0],
        [3, 7, 0, 0, 0, 0, 0, 0, 4],
        [9, 0, 0, 7, 0, 0, 1, 3, 0]]

    solution = [
        [4, 5, 3, 6, 2, 9, 8, 1, 7],
        [7, 1, 6, 8, 5, 4, 2, 9, 3],
        [8, 9, 2, 3, 1, 7, 4, 6, 5],
        [5, 3, 8, 9, 4, 1, 7, 2, 6],
        [6, 4, 7, 2, 3, 8, 9, 5, 1],
        [1, 2, 9, 5, 7, 6, 3, 4, 8],
        [2, 8, 1, 4, 6, 3, 5, 7, 9],
        [3, 7, 5, 1, 9, 2, 6, 8, 4],
        [9, 6, 4, 7, 8, 5, 1, 3, 2],
    ]

    actual = solve(puzzle)
    print_p(actual)
    print(actual and is_solved(actual), actual == solution)

def test_resolve():
    S = [
        [3, 4, 6, 1, 0, 0, 0, 0, 8],
        [0, 8, 0, 0, 9, 0, 0, 3, 0],
        [2, 0, 0, 0, 0, 5, 4, 0, 0],
        [4, 0, 0, 0, 0, 1, 8, 0, 0],
        [0, 3, 0, 0, 7, 0, 0, 4, 0],
        [0, 0, 7, 9, 0, 0, 0, 0, 3],
        [0, 0, 8, 4, 0, 0, 0, 0, 6],
        [0, 2, 0, 0, 5, 0, 0, 8, 0],
        [1, 0, 0, 0, 0, 2, 5, 0, 0],
    ]


    resolve(S)
    print('BAD' if is_bad(S) else 'OK')
    print_p(S)

def test_resolve_1():
    S = [
        [3, 0, 0, 1, 2, 7, 0, 0, 0],
        [7, 8, 5, 6, 9, 0, 1, 3, 0],
        [2, 1, 0, 3, 8, 5, 0, 6, 0],
        [0, 6, 2, 5, 3, 1, 0, 7, 9],
        [9, 0, 1, 2, 7, 8, 6, 0, 5],
        [8, 5, 0, 9, 0, 6, 2, 1, 3],
        [5, 9, 8, 0, 0, 3, 7, 2, 6],
        [6, 2, 0, 7, 0, 9, 0, 8, 1],
        [1, 7, 0, 8, 0, 2, 5, 9, 0]]

    C = candidates_for(S)
    print_p(S)
    print_c(C)
    resolve(S, C)
    print_c(C)

    print('BAD' if is_bad(S) else 'OK')
    print_p(S)

def test_resolve_2():
    S = [
        [3, 4, 6, 1, 2, 7, 9, 5, 8],
        [5, 8, 1, 6, 9, 4, 2, 3, 7],
        [2, 7, 9, 3, 8, 5, 4, 6, 1],
        [4, 5, 0, 0, 0, 1, 8, 0, 0],
        [0, 3, 0, 0, 7, 0, 0, 4, 0],
        [0, 0, 7, 9, 0, 0, 0, 0, 3],
        [0, 0, 8, 4, 0, 0, 0, 0, 6],
        [0, 2, 0, 7, 5, 0, 0, 8, 0],
        [1, 0, 0, 8, 0, 2, 5, 0, 0],
    ]

    C = candidates_for(S)
    print_p(S)
    print_c(C)
    resolve(S, C)
    print_c(C)

    print('BAD' if is_bad(S) else 'OK')
    print_p(S)

def test_candidates_for():
    S = [
        [1, 8, 6, 0, 0, 0, 0, 0, 0],
        [7, 5, 3, 0, 0, 0, 0, 0, 0],
        [4, 2, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]


    C = candidates_for(S)
    print(*[[list(bitset_iter(bs)) for bs in r] for r in C], sep='\n')


if __name__ == '__main__':
    # test_candidates_for()
    # test_resolve_1()
    # test_resolve_2()
    # test_1()
    # test_2()
    # test_3()
    # test_solve(ok_1)
    test_solve(ok_2)
    # test_solve(ok_3)
    # test_solve(wrong_1)
