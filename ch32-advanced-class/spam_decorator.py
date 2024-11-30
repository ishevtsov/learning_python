class Spam:
	numInstances = 0
	def __init__(self):
		Spam.numInstances += 1

	@staticmethod
	def printNumInstances():
		print(f'Number of instances created: {Spam.numInstances}')

a = Spam()
b = Spam()
c = Spam()

Spam.printNumInstances()