def get_decimals(num, den, stack =[]):
    if num == 0 or den == 0:
        return len(stack)
    elif num in stack:
        return len(stack) -1
    else:
        a,b = divmod(num, den)
        return get_decimals(b*10, den, stack+[num])

print  max((get_decimals(1, num), num) for num in range(2, 1001))

