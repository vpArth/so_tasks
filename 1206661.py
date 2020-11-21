sequences = [10,2,8,7,5,4,3,11,0,1]

result = [a if b is None or a > b else b for a, b in zip(sequences, sequences[1:]+[None])]

print(result)

result = list(map(lambda a, b: a if b is None or a > b else b, sequences, sequences[1:]+[None]))

print(result)
