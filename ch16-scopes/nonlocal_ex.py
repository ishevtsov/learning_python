def tester(start):
	state = start
	def nested(label):
		print(label, state)
	return nested

f = tester(0)
f('spam')
f('ham')