class X:
	def m(self):
		print('X.m')

class Y:
	def m(self):
		print('Y.m')

class C(X):
	def m(self):
		super().m()

i = C()
i.m()

C.__bases__ = (Y,)
i.m()