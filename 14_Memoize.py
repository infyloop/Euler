ans_memo = {}
def memo(k):
    if not k in ans_memo:
        ans_memo[k] =  Cycle(k,0)
	return ans_memo[k]

def Cycle(n,globCount):
	if(n == 1):
		return globCount
	else:
		globCount += 1
		if(n%2==0):
			return Cycle(n/2,globCount)
		return Cycle(3*n+1,globCount)

maxi = 1000001
num = 1
ans = 0
numCycle = -1000
while(num<maxi):
	new = memo(num)
	if(new>numCycle):
		numCycle = new
		ans = num
	num = num+1
print ans
