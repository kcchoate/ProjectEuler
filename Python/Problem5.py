def div(n):#checks to see if a number is divisible by all number 1-20
	for i in range(1,21):
		if n % i != 0:
			return False
	return True

number = 1
solved = False

while not solved:
	if div(number):
		print (number)
		solved = True
	number += 1
