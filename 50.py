from math import sqrt

def isPrime(n):
    if ((n%2 == 0) or (n%3 == 0) or (n == 1)):
        return False
    else:
        for i in range(5, int(sqrt(n))+1):
            if n%i == 0:
                return False
        return True

#maximum limit
#maxi = 1000000+1
maxi = 1000000+1

# generate primes
primes = [i for i in range(5, maxi) if isPrime(i)]
primes.insert(0, 2)
primes.insert(1, 3)
ln = len(primes)
print "primes generated"

max_sum = 0
max_len = 0

for i in range(0, ln):
    for j in range(0, i):
        s1 = sum(primes[j:i])
        curr_len = i-j
        if s1>max_sum and curr_len > max_len:
            if s1 in primes:
                max_sum = s1
                max_len = curr_len
                
        
print max_sum, max_len
        
            
