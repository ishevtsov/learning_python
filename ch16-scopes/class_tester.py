class Tester:
	def __init__(self, start):
		self.state = start

	def nested(self, label):
		print(label, self.state)
		self.state += 1

f = Tester(0)
f.nested('spam')
f.nested('ham')