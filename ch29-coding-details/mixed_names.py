class MixedNames:
	data = 'spam'

	def __init__(self, val):
		self.data = val

	def dispay(self):
		print(self.data, __class__.data)

x = MixedNames(1)
y = MixedNames(2)

x.dispay(); y.dispay()