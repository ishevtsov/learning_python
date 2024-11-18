def square(arg):
	return arg ** 2

class Sum:
	def __init__(self, val):
		self.val = val

	def __call__(self, arg):
		return self.val + arg

class Product:
	def __init__(self, val):
		self.val = val

	def method(self, arg):
		return self.val * arg

sobj = Sum(2)
pobj = Product(3)
actions = [square, sobj, pobj.method]

for act in actions:
	print(act(5))

print(actions[-1](5))

print('list comprehension: ', list([act(5) for act in actions]))

print('lambda: ', list(map(lambda act: act(5), actions)))