def fib_till(max):
    a, b = 0, 1
    data = []
    while b < max:
        
        a, b = b, a+b
        data.append(a)
    return data

print sum([el for el in fib_till(4000000) if el%2==0])

prev2 = 0
prev1 = 1
sum = 0
curr = 0
while(curr<4000000):
  curr = prev1 + prev2
  if(curr%2==0):
    sum += curr	
  prev2 = prev1
  prev1 = curr
print sum	

