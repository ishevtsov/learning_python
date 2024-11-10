class Callee:
	def __call__(self, *pargs, **kargs):
		print('Called:', pargs, kargs)

c = Callee()
c(1,2,3, a=1, b=2)