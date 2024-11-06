x = 11

def g1():
	print(x) # 11

def g2():
	global x
	x = 22	# changed global

def h1():
	x = 33
	def nested():
		print(x)

def h2():
	x = 33
	def nested():
		nonlocal x
		x = 44


if __name__ == '__main__':
	print(x)
	g1()
	g2()
	print(x)

