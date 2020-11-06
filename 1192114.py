for i in range(40):
	if i % 10 in (4, 7, 9, 0):
		continue
	print(i, end=' ')
print()

print(' '.join(map(str, [i for i in range(40) if i % 10 not in (4, 7, 9, 0)])))