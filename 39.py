lst = [0]*1001
for i in range(1, 1001):
    print i
    for a in range(1, i+1):
        for b in range(1, i+1):
            if a**2 + b**2 == (i-(a+b))**2:
                lst[i] += 1
print lst
print lst.index(max(lst))            
