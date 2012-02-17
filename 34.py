maxi = 10000000
facti = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
ans = 0
for i in range(10, maxi):
    b = map(int, str(i))
    if i == sum([facti[j] for j in b]):
        ans += i
        print i
print ans        
