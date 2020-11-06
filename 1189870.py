from functools import reduce

listt = [10, 7, 2, 12, 76, 100, 324]
control_number = 30


solution = sorted(filter(
	lambda x: int(x) < control_number, 
	reduce(
		lambda data,x: {'sums': data['sums'] + (data['prev']+x,) if data['prev'] is not None else tuple(), 'prev': x}, 
		listt, 
		{'sums': tuple(), 'prev': None}
	)['sums']
))

print(' '.join(map(str, solution)))
