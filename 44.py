from math import sqrt
import sys
def is_pent(n):
    if ((sqrt(24*n+1)+1)%6 == 0):
        return True
    return False
    
p = [-1, 1]
n = 2
while(1):
    p.append(n*(3*n-1)/2)
    for i in range(0, len(p)-1):
        if is_pent(p[n]-p[i]) and is_pent(p[n] + p[i]):
            print p[n] - p[i]
            sys.exit(0)
            break
    n += 1

    
    

