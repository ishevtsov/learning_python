def sumtree(l):
	tot = 0
	items = list(l)
	while items:
		print(tot, items)
		front = items.pop(0)
		if not isinstance(front, list):
			tot += front
		else:
			items[:0] = front
	return tot

l = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(l))