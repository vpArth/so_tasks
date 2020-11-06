from random import randint
randList = [randint(1, 100) for _ in range(10)]

a = b = c = float('-inf')
for el in randList:
	if el > a:
		a, b, c = el, a, b
	elif el > b:
		b, c = el, b
	elif el > c:
		c = el

# print(randList)
print('{}, {}, {}'.format(a, b, c))