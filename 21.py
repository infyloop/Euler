# sum of proper divisors
def pds(n):
    return sum(x for x in range(1, n//2+1) if not n%x)

#print d(284)
print sum(i for i in range(1, 10000) if pds(pds(i)) == i and i != pds(i))

