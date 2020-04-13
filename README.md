# Quick_Maths

[![Build Status](https://travis-ci.com/ntaff/Quick_Maths.svg?branch=master)](https://travis-ci.com/ntaff/Quick_Maths)[![codecov](https://codecov.io/gh/ntaff/Quick_Maths/branch/master/graph/badge.svg)](https://codecov.io/gh/ntaff/Quick_Maths)

This repository contain some mathematicals implementations : 

The repo now contain the following dir/files :

### Python
0. `lib/*.py` : Contains various functions

1. `Primality.py`: Contains primality stuff
   - `fermat_witness(n)` Check if n is composite, if yes, then return a fermat_witness (see [this article](https://en.wikipedia.org/wiki/Fermat_primality_test))
   - `miller_rabin_primtest(n,k)` [Miller-Rabin](https://fr.wikipedia.org/wiki/Test_de_primalit%C3%A9_de_Miller-Rabin) primality test
   - `prime_in_range(a,b)` Find a prime number in a given range (a --> b)
   - `is_prime(number)` Check if 'number' is prime
   - `getprime(nbits)` Generate a prime number that can be stored in 'nbits' bits.
   - `safe_prime(a,b)` Find a safe prime number in a given range [a; b[
   - `eratosthene()` Yields the sequence of prime numbers via the Sieve of Eratosthene
   - `sumPrimes(n)` Return the sum of the first n primes
   - `isCircularPrime(n)` Return true if n is a circular prime
   
2. `Arithmetic.py.py`: Contains arithmetic stuff
   - `gcd(p, q)` Return the greatest common divisor of p and q
   - `extd_pgcd(a, b)` Compute extended gcd of two integers (Extended Euclidean algorithm)
   - `linear_congruence(a, b, n)` Resolve linear congruence equations


### Caml
1. `Primality.ml`: Contains primality stuff
   
   
### Elixir
1. `Primality.exs`: Contains primality stuff
   - `PrimeFinder` Return the n-th prime number
