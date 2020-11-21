def compositions(n):
    result = []
    l = []
    l.append(n)
    while l is not None:
        result.append(l)
        l = getNextComposition(l, n)

    return result

def getNextComposition(prev, n):
    current = prev[:]
    for i in range(len(current)-1, -1, -1):
        if current[i] != 1:
            current[i] -= 1
            if len(current) > i+1:
                if len(current)-(i+1) > 1:
                    ones = 0
                    for j in range(len(current)-1, i, -1):
                        ones += current[j]
                    current[:] = current[0:i+1]
                    current.append(ones+1)
                else:
                    current[i+1] += 1
            else:
                current.append(1)
            return current

    return None

def foo(n, k = None):
    if k is None:
        k = n

    if n == 0:
        return []

    return ([[n]] if n<=k else []) + [
        l + [i]
        for i in range(1, 1+min(n, k))
        for l in foo(n-i, i)]

"""
int nf(int x, int k) {
  if (x == 0)
    return 1;
  int res = 0;
  for (int i = MIN(x, k); i > 0; --i)
    res += nf(x - i, i);
  return res;
}
"""
print(compositions(4))
print(*foo(5), sep='\n')
