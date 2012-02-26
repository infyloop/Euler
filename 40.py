maxi = 1000000 + 1
ans_str = ''
for i in range(1, maxi):
    ans_str += str(i)

prod = [];i = 1
while(i < maxi):
    print i
    prod.append(ans_str[i-1]); i*= 10

print prod
    
