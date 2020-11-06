ratio = 1<<200

def to_int(f):
    """ If not enough precision falls into 0 or Infinity values
    """
    # print(f, int(f * ratio), f*ratio)
    return int(f * ratio)

def to_float(d):
    return d / ratio


def to_int_2(f):
    r = (f * ratio).as_integer_ratio()
    print(r)
    assert r[1] == 1, 'Not enough precision'
    return r[0]

assert to_float(to_int(0.1) + to_int(0.2)) == 0.1 + 0.2
assert to_float(to_int(-1.03e-30) + to_int(-2.04e-31)) == (-1.234e-30)
assert to_float(to_int(-1.03e+130) + to_int(-2.04e+129)) == (-1.234e+130)


assert to_int(1e-300) == 0
try:
    print(to_int(1e+300))
except OverflowError as e:
    assert str(e) == 'cannot convert float infinity to integer'

assert to_float(to_int_2(0.1) + to_int_2(0.2)) == 0.1 + 0.2
assert to_float(to_int_2(0.05) + to_int_2(0.25)) == 0.3
assert to_float(to_int_2(-1.03e-30) + to_int_2(-2.04e-31)) == (-1.234e-30)
assert to_float(to_int_2(-1.03e+130) + to_int_2(-2.04e+129)) == (-1.234e+130)


try:
    to_int_2(1e-300) == 0
except AssertionError as e:
    assert str(e) == 'Not enough precision'
try:
    print(to_int_2(1e+300))
except OverflowError as e:
    assert str(e) == 'cannot convert Infinity to integer ratio'
