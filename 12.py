import math
def calcFactor(n):
	fact = 0
	root = int(math.sqrt(n))
	for i in range(2,root+1):
		if(n%i==0):
			fact = fact+1
	if(math.sqrt(n)==float(root)):
		return 2*fact+1
	else:
		return 2*(fact+1)
num = 1	
diff = 2
numFact = 0
while(numFact<501):
	numFact = calcFactor(num)
	#print numFact
	#print"    "
	num = num+diff
	diff = diff + 1
print num-diff
	
#http://projecteuler.net/index.php?section=problems&id=12
