from math import sqrt

def isPrime(n):
    if ((n%2 == 0) or (n%3 == 0) or (n == 1)):
        return False
    else:
        for i in range(5, int(sqrt(n))+1):
            if n%i == 0:
                return False
        return True

def is_perm(a, b, c):
    lsta = list(map(int, str(a)))
    lstb = list(map(int, str(b)))
    lstc = list(map(int, str(c)))
    lsta.sort(); lstb.sort(); lstc.sort()
    if lsta == lstb and lstb == lstc:
        return True
    return False
    
    

start = 1001; const = 3330;end = 9999; 
for i in range(start, end):
    a = i; b = i+const; c= i+2*const
    if is_perm(a, b, c):
        if isPrime(a) and isPrime(b) and isPrime(c):
            print str(a)+str(b)+str(c)

