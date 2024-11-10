class Commuter1:
	def __init__(self, val):
		self.val = val

	def __add__(self, other):
		print('add', self.val, other)
		return self.val + other

	def __radd__(self, other):
		print('radd', self.val, other)
		return other + self.val

class Commuter2:
	def __init__(self, val):
		self.val = val

	def __add__(self, other):
		print('add', self.val, other)
		return self.val + other

	def __radd__(self, other):
		return self.__add__(other)


class Commuter3:
	def __init__(self, val):
		self.val = val

	def __add__(self, other):
		print('add', self.val, other)
		return self.val + other

	def __radd__(self, other):
		return self + other

class Commuter4:
	def __init__(self, val):
		self.val = val

	def __add__(self, other):
		print('add', self.val, other)
		return self.val + other

	def __iadd__(self, other):
		self.val += other
		return self

	__radd__ = __add__


x = Commuter4(88)
y = Commuter4(99)

print(x + 1)
print(1 + y)
print(x + y)
x += 1
print(x.val)
