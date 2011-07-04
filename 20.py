ans = 1
for i in range(1,100):
	ans *= i
sum = 0
while(ans>0):
	sum = sum + ans%10
	ans /= 10
print sum
