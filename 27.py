import math

def isPrime(n):
	if(n%2 == 0):
		return 0
	for i in range(3,int(math.sqrt(n))+1):
		if(n%i == 0):
			return 0
        return 1
'''
for n = 0, we should get a prime, we can ensure the largest prime, 
by generating picking the max prime < 1000 hence b = 997
primes = [i for i in range(2, 1000) if isPrime(i)]
print primes[-1]
hence the max we can go is 997

now we simply put the equation as is and let my computer figure out the value. 
'''

primes = [i for i in range(2, 1000) if isPrime(i)]

maxi = 997+1
a_max = 0
b_max = 0
i_max = 0

def get_prods(a, b):
    global a_max
    global b_max
    global i_max
    i = 0
    while((i**2 + a*i + b) in primes):
        i += 1
        print a, b, i
    if(i>i_max):
        a_max = a
        b_max = b
        i_max = i
    return 0
    
for a in range(0, maxi):
    for b in range(0, maxi):
        get_prods(a, b)
        get_prods(a, -b)
        get_prods(-a, b)
                
print a_max*b_max                



