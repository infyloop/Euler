from math import sqrt

def isPrime(n):
    if ((n%2 == 0) or (n%3 == 0) or (n == 1)):
        return False
    else:
        for i in range(5, int(sqrt(n))+1):
            if n%i == 0:
                return False
        return True

maxi = 1000000+1


# generate primes
primes = [i for i in range(5, maxi) if isPrime(i)]
primes.insert(0, 2);primes.insert(1, 3);
print "primes generated"

uprime = maxi/2
while(not isPrime(uprime)):
    uprime -= 1
ulim = primes.index(uprime)

psum = [0]
for i in range(1, ulim+2):
    psum.append(psum[i-1] + primes[i-1])
ln = len(psum)

pset = set(primes)
terms = 0; maxp = 0
for i in range(ln-1, 0, -1):
    for j in range(0, i):
        if i-j > terms:
            chk = psum[i] - psum[j]
            if chk in pset:
                terms = i-j; maxp = chk

print terms, maxp

'''Runtime is pretty bad, needs improvement'''
