class Indexer:
	def __getitem__(self, index):
		return index ** 2

x = Indexer()
print(x[2])

for i in range(5):
	print(x[i], end=' ')