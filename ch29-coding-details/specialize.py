class Super:
	def method(self):
		print('in Super.method')

	def delegate(self):
		self.action()	# Expected to be defined

	def action(self):
		assert False, 'action must be defined!'

class Inheritor(Super):
	pass

class Replacer(Super):
	def method(self):
		print('in Replacer.method')

class Extender(Super):
	def method(self):
		print('starting Extender.method')
		Super.method(self)
		print('ending Extender.method')

class Provider(Super):
	def action(self):
		print('in Provider.action')


if __name__ == '__main__':
	for klass in (Inheritor, Replacer, Extender):
		print('\n' + klass.__name__ + '...')
		klass().method()
	print('\nProvider...')
	x = Provider()
	x.delegate()