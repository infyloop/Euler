maxi = 28123+1
# sum of proper divisors
def pds(n):
    return sum(x for x in range(1, n//2+1) if not n%x)

O = set(range(1, maxi))
#A set of abundant numbers, numbers are abundant if pds(n) > n
A = set([n for n in range(1, maxi) if pds(n) > n])

#B set of numbers which can be expressed as sum of two abundant numbers
B = set([a1+a2 for a1 in A for a2 in A if a1+a2<=maxi])

#C = O -B set of numbers which can't be expressed as sum of two abun nos. 
C = O - B

print sum(C)
