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

num_primes=1
current_num=2

while num_primes != 10001:
	current_num += 1
	if isprime(current_num):
		num_primes += 1
print (current_num)