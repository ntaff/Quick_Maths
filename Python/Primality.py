#Check if n is a composite, if yes, then return a fermat_witness
def fermat_witness(n):
  for a in range(2,n-2):
    if pow(a, n-1, n) != 1:
      return a

#Miller-Rabin primality test
def test_miller_rabin(n,k):
		for i in range(k):
			a = random.randint(2,n-2)
			if pow(a, n-1, n)!=1:
				return False
		return True
    
#Find a prime number in a given range (a --> b)
def prime_in_range(a,b):
  for i in range(a, b):
	  if test_miller_rabin(i,32):
		  return i	
   
