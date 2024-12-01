def fetcher(obj, index):
	 return obj[index]

def catcher():
	try:
		print(fetcher(x, 4))
	#except IndexError:
	#	print('got exception')
	finally:
		print('after fetch')
	print('continuing')

x = 'spam'
catcher()