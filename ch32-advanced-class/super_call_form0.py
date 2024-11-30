class C:
	def act(self):
		print('spam')

class D(C):
	def act(self):
		C.act(self)
		print('eggs')


x = D()
x.act()