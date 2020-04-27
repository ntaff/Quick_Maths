#Returns the greatest common divisor of p and q
def gcd(p, q):
	while q != 0:
		(p, q) = (q, p % q)
	return p

#Compute extended gcd of two integers (Extended Euclidean algorithm) v1
def extd_pgcd(a, b):
	r, r2 = a, b 
	u = v2 = 1
	u2 = v = 0
	while r2 != 0:
		q = r//r2
		rs, us, vs = r, u, v
		r, u, v = r2, u2, v2
		r2, u2, v2 = (rs - q*r2), (us - q*u2), (vs - q*v2)
	return u

#Compute extended gcd of two integers (Extended Euclidean algorithm) v2
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
	return (g, x - (b // a) * y, y)

#Resolve linear congruence equations
def linear_congruence(a, b, n):
	c = extd_pgcd(a, n)
	return ((c * (-b%n)) % n)

#Return inverse modular
def modinv(a, m):
		gcd, x, y = egcd(a, m)
		if gcd != 1:
			return None 
		else:
			return x % m

# Return if n is a quatratic residue of q
def is_quadratic_residue(q, n):
    for i in range(1, q):
        if (i**2 % q) == (n % q):
            return True
    return False

# Return the nth-digit Fibonacci number	
def fib(n):
	a, b = 1, 1
	term = 1
	while len(str(a)) < n:
		term += 1
		a, b = b, a + b
	return term

# Return the nth-digit Fibonacci number	(recursive way)
def recfibo(n):  
	if n <= 1:  
		return n  
	else:  
		return(recur_fibo(n-1) + recur_fibo(n-2))

# Return the nth-digit Fibonacci number	(iterator's way)
def fiboyield(n):
    a, b = 1, 1
    while b <= n:
        a, b = b, a + b
        yield a

# Return the sum of the nth-first even Fibonacci numbers
def sum_fibo_even(n):
    return sum(i for i in fib_generator(n) if not i % 2)
