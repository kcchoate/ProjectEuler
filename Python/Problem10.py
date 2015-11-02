def isprime(n): #obtained from StackOverflow, It uses the fact that a prime (except 2 and 3) is of form 6k-1 and 6k+1 and looks only at divisors of this form.
   """Returns True if n is prime"""
   if n == 2: return True
   if n == 3: return True
   if n % 2 == 0: return False
   if n % 3 == 0: return False

   i = 5
   w = 2
   while i * i <= n:
      if n % i == 0:
         return False

      i += w
      w = 6 - w

   return True

sum = 0

for i in range(2,2000000):
	if isprime(i):
		sum += i

print (sum)