''' We need to figure out an upper bound, since it is not given in the question. Let the number of digits in such a number be 'd'
(9^5)*d [A] will be the maximum sum of such a number.
This maximum sum will always be less than 10^(d-1) [B]

since A > B.
we can find the above relation holds true for d<= 6
hence we should go upto (9^5)*6

'''

high = 354294
chksum = lambda num: sum(int(i)**5 for i in str(num))
ans = sum(i for i in range(10, high+1) if i == chksum(i))
print ans
