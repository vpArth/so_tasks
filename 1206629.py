def solve(profile):
    if not profile:
        return 0
    l, r = 0, len(profile) - 1
    max_l, max_r = profile[l], profile[r]
    water = 0
    while l < r:
        if max_l >= max_r:
            water += max_r - profile[r]
            r -= 1

            max_r = max(max_r, profile[r])
        else:
            water += max_l - profile[l]
            l += 1

            max_l = max(max_l, profile[l])

    return water


print(solve([101, 1, 1, 2, 1, 101])) # 399
print(solve([2, 5, 2, 3, 6, 9, 3, 1, 3, 4, 6])) # 18
print(solve([1, 2, 3, 4, -11019, 4, 3, 2, 1])) # 11023
print(solve([])) # 0
