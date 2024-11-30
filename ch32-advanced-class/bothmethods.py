class Methods:
	def imeth(self, x):
		print([self, x])
	
	def smeth(x):
		print([x])

	def cmeth(cls, x):
		print([cls, x])

	smeth = staticmethod(smeth)
	cmeth = classmethod(cmeth)


obj = Methods()
obj.imeth(1)
Methods.imeth(obj, 2)

Methods.smeth(3)
obj.smeth(4)

Methods.cmeth(5)
obj.cmeth(6)
