'''
The case is as follows:
Master String = ABCDEFGHI
x*y = z
all the integers of x, y and z should contribute to 
the master string 'uniquely'
len(z) >= len(x) and len(z) >= len(y)
Hence we come to the following conclusion that the solution can always be of the 
form 
1) ABC*DE = FGHI
2) ABCD*E = FGHI
NOT  AB*CD = EFGHI
since 99 * 99 = 9801
'''

import itertools
strn = "123456789"
soln = []
perms = list(itertools.permutations(strn))

for perm in perms:
    num = ''.join(list(perm))
# processing form 1    
    n1 = int(num[0:3]); n2 = int(num[3:5]); n3 = int(num[5:]);
    if n1*n2 == n3 and n3 not in soln:
        soln.append(n3)
        print n1, n2, n3
# processing second form (not the html form)
    n1 = int(num[0:4]); n2 = int(num[4:5]); n3 = int(num[5:]);
    if n1*n2 == n3 and n3 not in soln:
        soln.append(n3)
        print n1, n2, n3

print sum(soln)

