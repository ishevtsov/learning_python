class C:
	def __getitem__(self, ix):
		print('C index')

class D(C):
	def __getitem__(self, ix):
		print('D index')
		C.__getitem__(self, ix)
		super().__getitem__(ix)
		super()[ix]

x = C()
x[99]

y = D()
y[99]