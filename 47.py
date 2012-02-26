from math import sqrt
import sys
def isPrime(n):
    if ((n%2 == 0) or (n%3 == 0) or (n == 1)):
        return False
    else:
        for i in range(5, int(sqrt(n))+1):
            if n%i == 0:
                return False
        return True

primes = [i for i in range(5, 1000000) if isPrime(i)]
primes.insert(0, 2)
primes.insert(1, 3)

print "primes generated"

def num_of_fact(n):
    np = 0; i = 0; 
    while(n >= 0 and n != 1):
        cnt = 0
        while(n%primes[i] == 0):
            n = n/primes[i]
            cnt = 1
        np += cnt
        i += 1
    return np

start = 646
one = num_of_fact(start) 
two = num_of_fact(start+1) 
three = num_of_fact(start+2)
start += 3

while(1):
    four = num_of_fact(start) 
    if one==two==three == four == 4:
        print start
        sys.exit(0)
    one = two;two = three; three = four 
    start += 1
