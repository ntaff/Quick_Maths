#Returns the greatest common divisor of p and q
def gcd(p, q):
	while q != 0:
		(p, q) = (q, p % q)
	return p

#Compute extended gcd of two integers (Extended Euclidean algorithm)
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

#Resolve linear congruence equations
def linear_congruence(a, b, n):
	c = extd_pgcd(a, n)
	return ((c * (-b%n)) % n)
