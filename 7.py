import math
max = 10001
cnt = 1
iter = 3
def isPrime(n):
	if(n%2 == 0):
		return 0
	root = int(math.sqrt(n))
	for i in range(3,root+1):
		if(n%i == 0):
			return 0
			break
	return 1
	
while(cnt<max):
	if isPrime(iter):
		cnt += 1			
		print iter
	iter += 1 

#http://projecteuler.net/index.php?section=problems&id=7
