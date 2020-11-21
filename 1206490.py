def solution0(a):
    result = 0
    for i in range(1, len(a)):
        a[i] += a[i-1]
        result += abs(a[i-1])

    return result

def solution(a):
    work = 0
    total = 0
    for w in a:
        total += w
        work += abs(total)

    return work

print(solution([5, -4, 1, -3, 1])) # 9
print(solution([-1000, -1000, -1000, 1000, 1000, 1000])) # 9000
print(solution([1, 0, 0, 0, -1])) # 4
print(solution([-1, 0, 0, 0, 1])) # 4
