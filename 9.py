for i in range(334,501):
	for j in range(500-i/2,i):
		k = 1000 - (i+j)
		if(i*i == (j*j + k*k)):
			print i*j*k
			break
#http://projecteuler.net/index.php?section=problems&id=9
