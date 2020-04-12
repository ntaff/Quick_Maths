from math import pow
import random
from lib.primlib import *
from itertools import takewhile

#Returns the greatest common divisor of p and q
def gcd(p, q):
	while q != 0:
		(p, q) = (q, p % q)
	return p

#Check if n is a composite, if yes, then return a witness
def fermat_witness(n):
	for a in range(2,n-2):
		if pow(a, n-1, n) != 1:
			return a

#Miller-Rabin primality test
def miller_rabin_primtest(n, k):
	#Prevent inf loop when d=0
	if n < 2:
		return False
	d = n - 1
	r = 0
	while not (d & 1):
		r += 1
		d >>= 1
	for _ in range(k):
		a = randint(n - 3) + 1
		x = pow(a, d, n)
		if x == 1 or x == n - 1:
			continue
		for _ in range(r - 1):
			x = pow(x, 2, n)
			if x == 1:
				return False
			if x == n - 1:
				break
		else:
			return False
	return True

# Check if 'number' is prime
def is_prime(number):
	if number < 10:
		return number in {2, 3, 5, 7}
	if not (number & 1):
		return False
	k = get_primality_testing_rounds(number)
	return miller_rabin_primality_testing(number, k + 1)

#Find a prime number in a given range [a; b[
def prime_in_range(a,b):
	for i in range(a, b):
		if miller_rabin_primtest(i,32):
			return i
		
#Generate a prime number that can be stored in 'nbits' bits.
def getprime(nbits):
	assert nbits > 3
	while True:
		integer = read_random_odd_int(nbits)
		if is_prime(integer):
			return integer

#Find a safe prime number in the given range [a; b[
def safe_prime(a,b):
	i = 0
	while True:    
		qs = 2*random.randint(a//24, b//24)+1
		while qs % 3 == 0 or qs % 5 == 0 or qs % 7 == 0 or qs % 11 == 0:
			qs = 2*random.randint(a//24, b//24)+1
		qp = 6*qs+3
		if miller_rabin_primtest(qp, 2):
			p = 12*qs + 7
			if miller_rabin_primtest(p, 2):
				return p
		qp = 6*qs + 5
		if miller_rabin_primtest(qp, 2):
			p = 12*qs + 11
			if miller_rabin_primtest(p, 2):
				return p
			
# Return true if n is a circular prime (prime where all rotations of the digits are themselves prime)
def isCircularPrime(n):
	n1 = str(n)*2
	for i in range(len(str(n))):
		if not is_prime(int(n1[i:len(str(n))+i])):
			return False
	return True

# Yields the sequence of prime numbers via the Sieve of Eratosthene
def eratosthene():
	yield 2
	D = {}
	q = 3
	while True:
		two_p = D.pop(q, None)
		if two_p:
			x = q + two_p
			while x in D:
				x += two_p
			D[x] = two_p       
		else:
			D[q*q] = 2*q     
			yield q
		q += 2

# Return the sum of the first n primes
def sumPrimes(n):
	return(sum(takewhile(lambda x: x < n, eratosthene())))
