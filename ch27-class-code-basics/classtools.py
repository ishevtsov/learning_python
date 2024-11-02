"Assorted class utilities and tools"

class AttrDisplay:
	"""
	Provides an inheritable display overload method that shows
	instances with their class names and a name=value pair for
	each attribute stored on the instance itself (but not attrs
	inherited from its classes). Can be mixed into any class,
	and will work on any instance.
	"""
	def __gatherAttrs(self):
		attrs = []
		for k in sorted(self.__dict__):
			attrs.append(f'{k}={getattr(self, k)}')
		return ', '.join(attrs)

	def __repr__(self):
		return f'[{self.__class__.__name__}: {self.__gatherAttrs()}]'

if __name__ == '__main__':
	class TopTest(AttrDisplay):
		count = 0
		def __init__(self):
			self.attr1 = TopTest.count
			self.attr2 = TopTest.count+1
			TopTest.count += 2

		def gatherAttrs(self):
			return 'Spam'

	class SubTest(TopTest):
		pass

	x, y = TopTest(), SubTest()
	print(x)
	print(y)