class B:
	def __init__(self):
		print('B.__init__')

class C:
	def __init__(self):
		print('C.__init__')

class D(B, C):
	pass

x = D()