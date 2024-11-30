class Spam:
	numInstances = 0
	def __init__(self):
		Spam.numInstances += 1

	def printNumInstances():
		print(f'Number of instances {Spam.numInstances}')
	printNumInstances = staticmethod(printNumInstances)


a = Spam()
b = Spam()
c = Spam()

Spam.printNumInstances()

a.printNumInstances()