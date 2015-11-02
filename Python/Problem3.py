from math import sqrt
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

i = 1
max_factor = 0
for i in range(1, int(sqrt(600851475143))):
	if 600851475143 % i == 0 and isprime(i):
		max_factor = i

print (max_factor)