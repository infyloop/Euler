#Version 2
div_3_5 = lambda x : x%3==0 or  x%5==0
print sum([el for el in range(1,1000) if div_3_5(el)])

#Version 1
sum = 0
for i  in range(1,1000):
  if i % 3 == 0:
	sum += i
  elif i%5 == 0:
	sum += i	
print sum
  
