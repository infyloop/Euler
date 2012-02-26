''' A simple bottom-up DP'''
N = 20+1
val = [[0 for i in range(0, N)] for j in range(0, N)]

#init 
for i in range(0, N):
    val [i][0] = val[0][i] = 1

for i in range(1, N):
    for j in range(1, N):
        val[i][j] = val[i-1][j] + val[i][j-1]

print val[N-1][N-1]

''' this problem is also an example of application of pascal's triange
reference: http://staff.argyll.epsb.ca/jreed/math30p/perms_combs/pathways.htm
the answer is (2N!)/(N!**2)
Analysis of the two approach:
in the first approach the complexity is O(n**2)
however in the second approach using a recusrsive methodology
nCr = n-1Cr-1 * n/r the solution can be obtained in 
O(n/2)
'''


