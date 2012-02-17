num = 1;den = 1;
for n in range(10, 100):
    for d in range(n+1, 100):
        if n%10 != 0 and d%10 != 0:
            n = float(n); d = float(d)
            num1, num2 = divmod(n, 10)
            den1, den2 = divmod(d, 10)
            if num2 == den1:
                chk1 = num1/den2
                chk2 = n/d
                if chk1 == chk2:
                    print n, d 
                    num *= n; den *= d;
                    
                    
print num, den

        
    
