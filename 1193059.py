
def orig(a, n):
    k = 0 
    x = [] 
    for i in range(1, n+1): 
        if i!=n: 
            if sum(a[:i])%i==0 and sum(a[i:])%(n-i)==0: 
                l = [str(sum(a[:i])/i)]*i + [str(sum(a[i:])/(n-i))]*(n-i) 
                if l not in x: 
                    k+=1 
                    x.append(l) 
    if sum(a)%n==0: 
        if [str(sum(a)/n)]*n not in x: 
            k+=1 
    return k

def solve(a, n):
    variants = set();
    l_sum, r_sum = 0, sum(a)

    for i in range(n):
        l_avg, l_rem = divmod(l_sum, i) if i else (0, 0)
        r_avg, r_rem = divmod(r_sum, n - i)


        if l_rem == r_rem == 0:
            # variants.add(','.join([str(l_avg)] * i + [str(r_avg)] * (n-i)))
            variants.add(f'{i}, {l_avg}, {r_avg}' if i and l_avg != r_avg else r_avg)

        l_sum += a[i]
        r_sum -= a[i]

    return len(variants)

a = [10, 4, 2, 7, 5, 8, 6, 6, 15] 
assert orig(a, len(a)) == 3
assert solve(a, len(a)) == 3

a = [3, 5, 2, 7, 6, 4, 5, 8, 1, 7] 
assert orig(a, len(a)) == 3
assert solve(a, len(a)) == 3
