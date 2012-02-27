import sys
from math import sqrt


def isPrime(n):
    if ((n%2 == 0)  or (n%3 == 0) or (n == 1)):
        return False
    else:
        for i in range(5, int(sqrt(n))+1):
            if n%i == 0:
                return False
        return True

maxi = 10000+1
primes = [i for i in range(1, maxi) if isPrime(i)]
primes.insert(0, 2)
primes.insert(1, 3)

def chk(n):
    for i in range(1, int(sqrt(n))+1):
        pchk = n - 2*(i**2)
        if pchk in primes:
            return True
    return False


for i in range(2, maxi):
    if not i in primes and (i%2 == 1):
        if not chk(i):
            print i
            sys.exit(0)


''' easiest way to check if a number is a perfect sqr        
sqrt(n).is_integer()
kept for reference
'''
