import math
def isPrime(n):
	if(n%2 == 0):
		return 0
	for i in range(3,int(math.sqrt(n))+1):
		if(n%i == 0):
			return 0
			break
	return 1
sum = 2
for i in range(3,2000000):
	if isPrime(i):
		sum += i
print sum
##http://projecteuler.net/index.php?section=problems&id=10
