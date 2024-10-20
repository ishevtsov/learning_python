def gensquares(n):
	for i in range(n):
		yield i ** 2


for i in gensquares(5):
	print(i, end=' : ')