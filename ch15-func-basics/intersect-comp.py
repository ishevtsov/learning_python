def intersect(seq1, seq2):
	return [x for x in seq1 if x in seq2]

s1 = "SPAM"
s2 = "SCAM"
print(intersect(s1, s2))