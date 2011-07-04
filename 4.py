import sys
max = 999;
min = 400;
ans = -233;
def ispalin(prod):
	string = str(prod)
	rev = string[::-1]
	if (rev == string):
        	return 1
    	else:
        	return 0

for i in range(min,max,1):
	for j in range(min,max,1):
		prod = i*j;
		if ispalin(prod) and prod>ans:
			ans = prod
			sys.exit
print ans
