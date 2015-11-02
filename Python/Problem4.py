def is_palindrome(x): #function to see if a number is a palindrome
	num = str(x)
	return num == num[::-1]

first_number = 0
second_number = 0
num = 0
for first_number in range(0,1000):
	for second_number in range(0,1000):#loop through every possible product
		product = first_number * second_number
		if product > num and is_palindrome(product):
			num = first_number * second_number

print (num)