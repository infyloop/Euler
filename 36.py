sum = 0
def is_palin(n):
    if n == n[::-1]:
        return True
    return False
        

for i in range(1, 1000001):
    if is_palin(str(i)):
        if is_palin(bin(i)[2:]):
            sum += i

print sum
