#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
from math import sqrt

def isprime(number):
	if((number % 2 == 0) or (number % 3 == 0) or (number<2)):
		return 0
	else:
		for i in range(4, int(sqrt(number))+1):
	 		if(number % i == 0):
	 			return 0
		return 1
		

        
	
num = 600851475143
root = int(sqrt(num))
for n in range(root, 1, -1):
 	if((num%n == 0) and isprime(n)):
		print n	   
        	break
  
