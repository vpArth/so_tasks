from math import ceil

def ariphm_sum(start, stop, step=1):
	""" Сумма арифметической прогрессии
		Аргументы аналогичны функции range, т.е. [start, stop) с шагом step

	"""
	n = ceil((stop - start) / step)
	return (start + step*(n-1)/2) * n

assert ariphm_sum(1, 101) == 5050
assert ariphm_sum(-100, 0) == -5050
assert ariphm_sum(-100, 101) == 0
assert ariphm_sum(1, 8, 2) == 16
assert ariphm_sum(1, 10, 2) == 25
assert ariphm_sum(-3, 10, 2) == 21
assert ariphm_sum(-3, 10, 3) == 15
assert ariphm_sum(-10**8, 10**8+1) == 0
assert ariphm_sum(-10**8, 10**8+2) == 100000001



# 1 2 3 4 5 (1, 6, 1)  = 15
# 1 3 5 7 9 (1, 10, 2) = 25
# -3 -1 1 3 5 7 9 (-3, 10, 2) = 21
# -3 0 3 6 9 (-3, 10, 3) = 15