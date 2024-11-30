class A:
	def __init__(self):
		print('A.__init__')

class B(A):
	def __init__(self):
		print('B.__init__')
		A.__init__(self)

class C(A):
	def __init__(self):
		print('C.__init__')
		A.__init__(self)

class D(B, C):
	pass

x = D()
