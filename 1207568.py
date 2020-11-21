def rev(fn):
    def inner(*args):
        return fn(*args)[::-1]
    return inner

@rev
def transform(list1, list2):
  result = []
  for i in list1:
     for j in list2:
        result.append(f"{i} + {j}")
  return result

res = transform([1, 2, 3], [5, 6, 7])

print(res)
