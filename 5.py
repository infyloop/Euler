def gcd(a,b):
	if(b==0):
		return a
	return gcd(b,a%b)
def lcm(a,b):
	return b*a/gcd(a,b)
ans = 2
for i in range(3,20):
	ans = lcm(ans,i)
print ans 
	
#http://projecteuler.net/index.php?section=problems&id=5

