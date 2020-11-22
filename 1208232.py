from collections import deque

def sorting(numbers):
    deques = [deque() for _ in range(10)]
    maxlen = 0
    i = 0
    result = numbers[:]
    while True:
        for number in result:
            n_str = str(number)
            l_str = len(n_str)
            digit = int(n_str[l_str - i - 1]) if i < l_str else 0
            deques[digit].append(number)
            maxlen = max(maxlen, l_str)

        result = []
        for d in deques:
            while d:
                result.append(d.popleft())

        i += 1
        if i >= maxlen:
            break


    return result



print(sorting([39, 47, 54, 59, 100, 34, 5, 41, 32, 20, 17]))
