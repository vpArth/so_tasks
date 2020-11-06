input() # skip N
l = map(int, input().split(' '))


min_velocity = 300
max_velocity = 1
less30 = 0
for x in l:
    if x > max_velocity:
        max_velocity = x
    if x < min_velocity:
        min_velocity = x
    if x <= 30:
        less30 += 1

print(max_velocity - min_velocity)
print(less30)