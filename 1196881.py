def compareWithNones(A, B):
    for i, row in enumerate(A):
        for j, cell in enumerate(row):
            b_cell = B[i][j]
            if cell is not None and b_cell is not None and cell != b_cell:
                return False
    return True


_ = None  # 0 or 1
A = [
    [1, _, 1, _],
    [0, 1, _, 0],
    [_, 1, 1, 0],
    [0, 0, 0, 0]
]

B = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 0]
]

C = [
    [_, 1, 1, 0],
    [0, 1, 0, 0],
    [1, _, 1, 0],
    [0, 0, _, 0]
]


print(compareWithNones(A, B)) # False
print(compareWithNones(A, C)) # True
