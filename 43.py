import itertools
strn = '0123456789'
primes = [-1, -1, 2, 3, 5, 7, 11, 13, 17]

def chk_num(strn):
    for i in range(2, 9):
        num = int(strn[i-1:i+2])
        if num%primes[i] != 0:
            return False
    return True

#print chk_num('1406357289')

perm = list(itertools.permutations(strn))
lst = [''.join(tpls) for tpls in perm]
ans = [int(strn) for strn in lst if chk_num(strn)]
print ans
print sum(ans)

