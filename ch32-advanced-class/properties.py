class properties:
	@property
	def age(self):
		return 40

	@age.setter
	def age(self, value):
		print(f'set age: {value}')
		self._age = value

x = properties()
x.age

x.age = 42

print(x._age)