import math
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

def l_check(n):
    lst = [int(i) for i in str(n)]
    for i in range(0, len(lst)):
        n = lst[0:i+1]
        nn = int(''.join(map(str, n)))
        if not isPrime(nn):
            return False
    return True
            
def r_check(n):
    lst = [int(i) for i in str(n)]
    ln = len(lst)
    for i in range(0, ln):
        n = lst[ln-i-1:ln]
        nn = int(''.join(map(str, n)))
        if not isPrime(nn):
            return False
    return True
    
sum = 0;cnt = 1;i = 10;
while(cnt<=11):
    i += 1
    if isPrime(i):
        if l_check(i):
            if r_check(i):
                sum += i
                cnt += 1
                print i, cnt

print sum

