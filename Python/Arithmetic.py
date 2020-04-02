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
