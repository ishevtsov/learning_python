class Adder:
	def __init__(self, val=0):
		self.data = val

	def __add__(self, other):
		return self.data + other

x = Adder(5)
print(x + 2)
# print(2 + x) Error: