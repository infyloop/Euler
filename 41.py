import itertools, sys, math
src = [1234567, 123456, 12345, 1234, 123, 12]


def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if(n%2 == 0):
        return False
    root = int(math.sqrt(n))
    for i in range(3,root+1):
        if(n%i == 0):
            return False
    return True

primes = [i for i in range(2, 7654321+1) if isPrime(i)]
print "prime gen"

'''
b = list(itertools.permutations('1234567'))
lst = [ int(''.join(tp)) for tp in b ]
for num in lst:
    if num in primes:
        print num, "here"
'''

ans = []
for i in src:
    b = list(itertools.permutations(str(i)))
    lst = [ int(''.join(tp)) for tp in b ]
    for num in lst:
        if num in primes:
            ans.append(num)
            sys.exit(0)
                
print max(ans)

            
             
    
