def sum(seq):
	def add(x,y): return x+y
	return reduce(add,seq,10)

print sum(range(1,11))
print sum([])