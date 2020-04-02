from math import pow
import random
			
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
    
#Find a prime number in a given range [a; b[
def prime_in_range(a,b):
	for i in range(a, b):
		if test_miller_rabin(i,32):
			return i
		
#Find a safe prime number in a given range [a; b[
def safe_prime(a,b):
	i = 0
	while True:    
		qs = 2*random.randint(a//24, b//24)+1
		while qs % 3 == 0 or qs % 5 == 0 or qs % 7 == 0 or qs % 11 == 0:
			qs = 2*random.randint(a//24, b//24)+1
		qp = 6*qs+3
		if test_miller_rabin(qp, 2):
			p = 12*qs + 7
			if test_miller_rabin(p, 2):
				return p
		qp = 6*qs + 5
		if test_miller_rabin(qp, 2):
			p = 12*qs + 11
			if test_miller_rabin(p, 2):
				return p
   
