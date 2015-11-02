total = 0
firstfib=2 #we will save the previous two fib numbers to prevent recalulation
secondfib=1
total = 2
n = 0
while n <= 4000000:
	n = firstfib + secondfib#calculate new fib to add to sum
	secondfib = firstfib#then save previous 2 fibs
	firstfib = n
	if n % 2 == 0:
	    total += n
print (total)