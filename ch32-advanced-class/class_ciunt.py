def count(aClass):
	aClass.numInstances = 0
	return aClass

@count
class Spam:
	pass

class Sub(Spam):
	pass

x = Spam()
y = Spam()
z = Spam()

print(Spam.numInstances)