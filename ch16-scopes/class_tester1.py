class Tester:
	def __init__(self, start):
		self.state = start

	def __call__(self, label):
		print(label, self.state)
		self.state += 1

f = Tester(99)
f('spam')
f('ham')
f('pancakes')