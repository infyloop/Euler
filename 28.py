'''Creating one more cycle of numbers, will show us an order,
which will eventually reduce the computation which
we need to perform. 

the series from bottom left to top right:
43 21 7 1 3 13 31
re-arranged it looks like this: 1 3 7 13 21 31 43
the difference between the difference of numbers increases by 2
1+2
3+4
7+6
13+8
etc. 


the series from top left to bottom right
37 17 5 1 9 25 49
re-arranged it looks like: 1 5 9 17 25 37 49
the difference between the difference of numbers increases by 4 at a cycle length of 2
1+4
5+4

9+8
17+8

25+12
37+12
etc. 
'''
s1 = s2 = 0;maxi = 1001;diff1 = 2;diff2 = 4;l1 = [1];l2 = [1]

for cnt in range(1, maxi):
    l2.append(l2[-1]+diff2)
    if not (cnt&1): diff2+=4
#print l2

for cnt in range(1, maxi):
    l1.append(l1[-1]+diff1)
    diff1 += 2
#print l1
# removing an extra 1 since in both list1 and list2 one has occured. 
print sum(l1) + sum(l2) - 1

