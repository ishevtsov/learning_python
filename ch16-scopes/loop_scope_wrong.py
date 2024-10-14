def makeActions():
	acts = []
	for i in range(5):
		acts.append(lambda x: i ** x)
	return acts

acts = makeActions()
print(acts[0])
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[4](2))