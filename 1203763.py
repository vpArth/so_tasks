def remove_before(l, v):
    try:
        i = l.index(v)
        return l[i:]
    except:
        return l[:]

assert remove_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
assert remove_before([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5]
assert remove_before([], 0) == []
