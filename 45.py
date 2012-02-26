import sys
from math import sqrt
start = 144

def is_tr(n):
    if ((-1 + sqrt(8*n+1))%2 == 0):
        return True
    return False


def is_pent(n):
    if ((sqrt(24*n+1)+1)%6 == 0):
        return True
    return False


def calc_hex(n):
    return n*(2*n-1)

while(1):
    val = calc_hex(start)
    if is_tr(val) and is_pent(val):
        print val
        sys.exit(0)
    start += 1

