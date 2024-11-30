class Spam:
	numInstances = 0
	def __init__(self):
		Spam.numInstances += 1

	def printNumInstances(cls):
		print(f'Number of instances: {cls.numInstances}')
	printNumInstances = classmethod(printNumInstances)

Spam.printNumInstances()

a, b = Spam(), Spam()
a.printNumInstances()
Spam.printNumInstances()