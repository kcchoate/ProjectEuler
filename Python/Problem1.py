total = 0
for n in range(0,1000):
	if n % 5 == 0 or n % 3 == 0:
		total += n
print (total)