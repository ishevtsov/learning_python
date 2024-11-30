class C:
	def act(self):
		print('spam')

class D(C):
	def act(self):
		super().act()
		print('eggs')

x = D()
x.act()

class E(C):
	def method(self):
		proxy = super()
		print(proxy)
		proxy.act()

E().method()
