import math
maxi = 1000000+1
lst = range(2, maxi)
ans = []


def isPrime(n):
	if(n%2 == 0):
		return 0
	for i in range(3,int(math.sqrt(n))+1):
		if(n%i == 0):
			return 0
        return 1

primes = [i for i in lst if isPrime(i)]
print "primes generated"

def chk_circ(num):
    s = str(num)
    perms = [int(s[i:] + s[:i]) for i in range(len(s))]
    for numstr in perms:
        if numstr not in primes:
            return False
    for numstr in perms:
        ans.append(numstr)
    return True
[chk_circ(i) for i in primes if i not in ans]
print ans  
print len(ans)

