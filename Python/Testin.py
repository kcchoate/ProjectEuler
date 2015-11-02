from math import sqrt
def count_divisors(n):
	num_divisors = 0
	for i in range(1, int(sqrt(n))):
		if n % i == 0:
			num_divisors += 2 #we only go to sqrt(n) so we count each divisor twice, once for itself and once for the other number to multiply by to get n
	return num_divisors

print (count_divisors(76576500))