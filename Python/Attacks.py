import hashlib
import string
import random
import time
from math import pow
from lib.primlib import *
import arithmetic
from itertools import takewhile
from functools import reduce

# Find collisions faster than the usual comparison method with the birthday paradox
# Parameter `bit_range` is the number of bits you want to collide
# TO-DO : use Rho method to reduce the complexity
def birthday_collisions_attack(bit_range):
    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str.encode()
        space_size = bit_range//4
    for i in range(100):
        t1 = time.time()
        lookup_table = {}
        # Optimalement 2**(bit_range//2)
        for _ in range(60000000):
            random_binary = get_random_string(12)
            result = hashlib.sha256(random_binary).hexdigest()[:space_size]
            lookup_table[result] = random_binary
        for _ in range(60000000):
            random_binary2 = get_random_string(12)
            result2 = hashlib.sha256(random_binary2).hexdigest()[:space_size]
            if result2 in lookup_table and lookup_table[result2] != random_binary2:
                print(random_binary2)
                print(lookup_table[result2])
                break
        t2 = time.time()
        print(t2-t1)

        
 #Crack a RSA private key if one of n factor is < 1e9
def rsa_attack_small_primes(pathpubkey, outputname):
	public_key = RSA.importKey(open(pathpubkey, 'r').read())
	n, e = public_key.n, public_key.e
	def factorprime(an):
		return n%an == 0
	for i in filter(factorprime, takewhile(lambda x: x < 1e9, eratosthene())):q=i
	p = n//q
	phi = (p -1)*(q-1)
	d = arithmetic.modinv(e,phi)
	private_key = RSA.construct((n, e, d))
	privkey = private_key.exportKey('PEM').decode()
	pkey= open(outputname,"w")
	pkey.write(privkey)
	pkey.close()

#Crack a RSA private key if one of n factor is < 1e14
def rsa_pollard_attack(pathpubkey, outputname): 
	def PollardRho(n): 
		if (n == 1): 
			return n   
		if (n % 2 == 0): 
			return 2 
		x = (random.randint(0, 2) % (n - 2)) 
		y = x  
		c = 1 
		d = 1 
		while (d == 1):  
			x = (pow(x, 2, n) + c + n)%n  
			y = (pow(y, 2, n) + c + n)%n 
			y = (pow(y, 2, n) + c + n)%n 
			d = math.gcd(abs(x - y), n) 
			if (d == n): 
				return PollardRho(n)   
		return d 
	public_key = RSA.importKey(open(pathpubkey, 'r').read())
	n, e = public_key.n, public_key.e
	q = PollardRho(n)
	p = n//q
	phi = (p -1)*(q-1)
	d = arithmetic.modinv(e,phi)
	private_key = RSA.construct((n, e, d))
	privkey = private_key.exportKey('PEM').decode()
	pkey= open(outputname,"w")
	pkey.write(privkey)
	pkey.close()
