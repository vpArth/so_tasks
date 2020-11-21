def solution0(n):
    result = 0
    for i in range(1, n+1):
        if i == 1:
            result += 1
        elif i == n:
            result += len(str(n))
        elif i % 10 == 0:
            result += len(str(i))

    return result

def solution1(n):
    result = (n > 0) + (n > 1) * len(str(n))
    for i in range(10, n, 10):
        result += len(str(i))

    return result

def solution2(n):
    result = (n > 0) + (n > 1 and n % 10 != 0) * len(str(n))

    k = n // 10

    result += k # последних цифр

    for i in range(1, k +1): # перебираем подряд числа без последнего нуля
        result += len(str(i))

    return result

def solution3(n):
    result = (n > 0) + (n > 1 and n % 10 != 0) * len(str(n))

    k = n // 10

    result += k

    if k < 9:
        result += k
    elif k < 99:
        result += 9 + 2*(k-9)
    elif k < 999:
        result += 189 + 3*(k-99)
    elif k < 9999:
        result += 2889 + 4*(k-999)
    elif k < 99999:
        result += 38889 + 5*(k-9999)
    elif k < 999999:
        result += 488889 + 6*(k-99999)
    elif k < 9999999:
        result += 5888889 + 7*(k-999999)

    return result

def solution4(n):
    result = (n > 0) + (n > 1 and n % 10 != 0) * len(str(n))

    k = n // 10

    result += k

    steps = (0, 9, 99, 999, 9999, 99999, 999999, 9999999)
    for stepi in range(1, len(steps)):
        S = ((stepi-1)*(10**stepi)-stepi*10**(stepi-1)+1) // 9 # https://oeis.org/A033713
        if k < steps[stepi]:
            result += S + (stepi)*(k - steps[stepi-1])
            break

    return result

def solution(n):
    result = (n > 0) + (n > 1 and n % 10 != 0) * len(str(n))

    k = n // 10

    result += k # все последние нули

    # Количество цифр от 1 до k
    i = 1
    while i <= k:
        result += k - i + 1
        i *= 10

    return result




for n, x in [
    (0, 0), (1, 1), (20, 5), (23, 7), (100, 22), (100000, 48895),
    (int(1e6), 588896) # , (int(1e7)-1, 6888896)
]:
    print('0', solution0(n), x)
    print('1', solution1(n), x)
    print('2', solution2(n), x)
    print('3', solution3(n), x)
    print('4', solution4(n), x)
    print(' ', solution(n), x)

