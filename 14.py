maxi = 1000001
num = 1
numCycle = -1000
def Cycle(n,globCount):
	if(n == 1):
		return globCount
	else:
		globCount += 1
		if(n%2==0):
			return Cycle(n/2,globCount)
		return Cycle(3*n+1,globCount)
while(num<maxi):
	new = Cycle(num,0)
	if(new>numCycle):
		numCycle = new
		ans = num
	num = num+1
print ans
#http://projecteuler.net/index.php?section=problems&id=14
#837799
