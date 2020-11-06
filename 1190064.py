
def solve():
	solution = []
	def hanoi(n, S, D, M=None):
		if n == 0:
			return
		V = (set(['A', 'B', 'C']) - set([S, D])).pop()
		hanoi(n-1, S, V, M)
		if M is None or M in [S, D]:
			solution.append([n, S, D])
		else:
			solution.append([n, S, M])
			solution.append([n, M, D])

		hanoi(n-1, V, D, M)


		return solution
	return hanoi

assert solve()(3, 'A', 'C') == [[1, 'A', 'C'], [2, 'A', 'B'], [1, 'C', 'B'], [3, 'A', 'C'], [1, 'B', 'A'], [2, 'B', 'C'], [1, 'A', 'C']]
assert solve()(2, 'A', 'B', 'B') == [[1, 'A', 'B'], [1, 'B', 'C'], [2, 'A', 'B'], [1, 'C', 'B']], solve()(2, 'A', 'B', 'B')

