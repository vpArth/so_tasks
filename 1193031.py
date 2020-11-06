def solution(inp):
    pattern = inp[0]
    for i, l in enumerate(inp[1:]):
        replacement = []
        for j, e in enumerate(pattern): 
            expected = f'{e[0]}{i+2}'
            replacement.append(expected if expected in l else e)
        l[:] = replacement
        pattern = l

    return inp


def zhihar(inp):
    # определить максимальный размер строк
    max_len = len(max(inp, key=len))

    # сформировать хранилище добавочных элементов
    storage = [''] * max_len
    # добавить новые элементы
    for obj in inp:
        # вычислить кол-во элементов, которые требуется добавить
        new_len = max_len - len(obj)

        # добавить недостающие элементы
        obj[:] = storage[:new_len] + obj
        # обновить хранилище
        storage = obj

    return inp

def extrn(inp):
    import itertools
    def complement(x, y):
        return x[:-len(y)] + y or x

    return list(itertools.accumulate(inp, complement))


def cases():
    inp = [
        ['A1', 'B1', 'C1', 'D1', 'E1'],
        ['C2', 'D2', 'E2'],
        ['D3', 'E3'],
        ['A4', 'B4', 'C4', 'D4', 'E4'],
        ['C5', 'D5', 'E5'],
        ['D6', 'E6'],
        ['C7', 'D7', 'E7'],
    ]

    expected = [
        ['A1', 'B1', 'C1', 'D1', 'E1'],
        ['A1', 'B1', 'C2', 'D2', 'E2'],
        ['A1', 'B1', 'C2', 'D3', 'E3'],
        ['A4', 'B4', 'C4', 'D4', 'E4'],
        ['A4', 'B4', 'C5', 'D5', 'E5'],
        ['A4', 'B4', 'C5', 'D6', 'E6'],
        ['A4', 'B4', 'C7', 'D7', 'E7'],
    ]

    yield (inp, expected, 'orig')
    yield ([['A1', 'B1', 'C1'], ['B2', 'C2'], ['C3']], [['A1', 'B1', 'C1'], ['A1', 'B2', 'C2'], ['A1', 'B2', 'C3']], 'tail')
    yield ([['A1', 'B1', 'C1'], ['B2'], ['C3']], [['A1', 'B1', 'C1'], ['A1', 'B2', 'C1'], ['A1', 'B2', 'C3']], 'any')

from copy import deepcopy

for inp, expected, title in cases():
    for (fn_name, fn) in {'my': solution, 'extrn': extrn, 'zhihar': zhihar}.items():
        try:
            assert fn(deepcopy(inp)) == expected
        except AssertionError as e:
            print(f'Error in {fn_name}({title})')            
        
