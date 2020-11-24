# from lib.bitmap import BitSet
BitSet = set

def copy(p):
    return [row[:] for row in p]

def row(p, n):
    return p[n]
def col(p, n):
    return list(map(lambda row: row[n], p))
def sqr(p, *args):
    if len(args) == 1:
        row, col = args[0] // 3, args[0] % 3
    else:
        row, col = args[0] // 3, args[1] // 3

    return [p[i][j] for i in range(3*row, 3*row+3) for j in range(3*col, 3*col+3)]

def candidates_for(p):
    rows = [BitSet(range(1, 10)) for _ in range(9)]
    cols = [BitSet(range(1, 10)) for _ in range(9)]
    sqrs = [BitSet(range(1, 10)) for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if p[i][j] != 0:
                rows[i].discard(p[i][j])
                cols[j].discard(p[i][j])
                sqrs[(i//3)*3+j//3].discard(p[i][j])

    return [[rows[i].intersection(cols[j]).intersection(sqrs[(i//3)*3+j//3]) if p[i][j] == 0 else BitSet([p[i][j]]) for j in range(9)] for i in range(9)]


def candidates(p, i, j):
    return (all_
        - BitSet(row(p, i))
        - BitSet(col(p, i))
        - BitSet(sqr(p, i, j))
        )

def is_bad(p, C = None):
    for i in range(9):
        if C:
            for j in range(9):
                if not C[i][j]:
                    return True

        for digit in range(1, 10):
            if (
                row(p, i).count(digit) > 1
                or col(p, i).count(digit) > 1
                or sqr(p, i).count(digit) > 1
            ):
                return True
    return False

def count_zeroes(p):
    return sum([row.count(0) for row in p])

def is_solved(p):
    if is_bad(p):
        return False

    return count_zeroes(p) == 0

def print_p(p):
    print('-'*9*3, *(p if p else [p]), sep='\n')

def exclude(C, i, j, d):
    for t in range(9):
        if t != j:
            C[i][t].discard(d)
        if t != i:
            C[t][j].discard(d)
        si, sj = i//3*3+t//3, j//3*3+t%3
        if si != i or sj != j:
            C[si][sj].discard(d)

def c_count(C, i, j, d):
    s = 0
    for t in range(9):
        if t != j:
            s += d in C[i][t]
        if t != i:
            s += d in C[t][j]
        si, sj = i//3*3+t//3, j//3*3+t%3
        if si != i or sj != j:
            s += d in C[si][sj]

    return s



def resolve(p, C = None):
    C = candidates_for(p) if C is None else C

    changing = True
    while changing:
        changing = False
        for i in range(9):
            for j in range(9):
                # Find only candidates
                if p[i][j] == 0:
                    if len(C[i][j]) == 1:
                        d = list(C[i][j])[0]
                        p[i][j] = d
                        changing = True
                        exclude(C, i, j, d)
                    # else:
                    #     # Find except candidates
                    #     for d in C[i][j]:
                    #         if c_count(C, i, j, d) == 0:
                    #             p[i][j] = d
                    #             C[i][j] = BitSet([d])
                    #             changing = True
                    #             exclude(C, i, j, d)



def sudoku_solver(puzzle):
    solution = copy(puzzle)
    C = candidates_for(solution)
    resolve(solution, C)

    if is_bad(solution, C):
        return None

    if count_zeroes(solution) == 0:
        return solution

    for i in range(9):
        for j in range(9):
            if solution[i][j] == 0:
                # for d in C[i][j]: # ;( Much longer than full range
                for d in range(1, 10):
                    solution[i][j] = d
                    res = sudoku_solver(solution)
                    if res is not None:
                        return res


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

    actual = sudoku_solver(puzzle)
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

    actual = sudoku_solver(puzzle)
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

    actual = sudoku_solver(puzzle)
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
        [3, 4, 6, 1, 2, 7, 9, 5, 8],
        [7, 8, 5, 6, 9, 4, 1, 3, 2],
        [2, 1, 9, 3, 8, 5, 4, 6, 7],
        [4, 6, 2, 5, 3, 1, 8, 7, 9],
        [9, 3, 1, 2, 7, 8, 6, 0, 5],
        [8, 5, 7, 9, 4, 6, 2, 1, 3],
        [5, 9, 8, 4, 1, 3, 7, 2, 6],
        [6, 2, 4, 7, 5, 9, 3, 8, 1],
        [1, 7, 3, 8, 6, 2, 5, 9, 4]]

    C = candidates_for(S)
    print_p(C)
    resolve(S, C)
    print_p(C)

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
    print_p(C)


if __name__ == '__main__':
    # test_candidates_for()
    # test_resolve_1()
    # test_1()
    # test_2()
    test_3()
