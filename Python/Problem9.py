def is_triplet (a, b, c):
	return a ** 2 + b ** 2 == c ** 2

for a in range(1,1001):
	print (a)
	for b in range(1,1001):
		for c in range(1,1001):
			if a + b + c == 1000 and is_triplet(a, b, c):
				print (a*b*c)