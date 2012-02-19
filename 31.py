''' 
This is the most famous coin change DP problem
'''
coins = [1, 2, 5, 10, 20, 50, 100, 200]
maxi = 200
lst = [1] + [0] * (maxi + 1)
[lst.__setitem__(i, lst[i] + lst[i - c]) for c in coins for i in range(c, maxi+1)]
print lst[200]





