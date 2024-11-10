class Indexer:
	data = [5, 6, 7, 8, 9]

	def __getitem__(self, index):
		print('getitem:', index)
		return self.data[index]

x = Indexer()
print(x[0])
print(x[1])
print(x[-1])

print(x[2:4])
print(x[1:])
print(x[:-1])
print(x[::2])
