class Node:
	def __init__(self, left, right):
		self.right = right
		self.left = left
	def __str__(self):
		return f'Node({self.left}, {self.right})'


def count_same(sub, tree):
	def is_same(sub, tree):
		if sub is None:
			return tree is None

		return (tree is not None 
			and is_same(sub.left, tree.left) 
			and is_same(sub.right, tree.right))

	if sub is None:
		return (1 if tree is None 
			else count_same(sub, tree.right) + count_same(sub, tree.left))


	if tree is None:
		return 0

	return (count_same(sub, tree.right) 
		+ count_same(sub, tree.left) 
		+ int(is_same(sub.left, tree.left) and is_same(sub.right, tree.right))
	)



tree1 = Node ( Node ( None , None ), Node ( None , None )) 
tree2 = Node ( None , Node ( Node ( None , None ), Node ( None , None ))) 

res = count_same(tree1, tree2)
assert res == 1, f'assert {res} == 1'
 
tree1 = Node ( None , None )
tree2 = Node ( None , Node ( Node ( None , None ), Node ( None , None ))) 

res = count_same(tree1, tree2)
assert res == 2, f'assert {res} == 2'
   
tree1 = None
tree2 = Node ( None , Node ( Node ( None , None ), Node ( None , None ))) 

res = count_same(tree1, tree2)
assert res == 5, f'assert {res} == 5'
   
tree1 = Node ( Node ( None , None ), Node ( None , None )) 
tree2 = Node ( Node ( None , None ), Node ( Node ( None , None ) , None )) 

res = count_same(tree1, tree2)
assert res == 0, f'assert {res} == 0'
