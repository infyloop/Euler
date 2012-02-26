Len = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve',
13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty',70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred'}

#for i in range(1, 1001):
def gen_num(n, stack=[]):
    if n == 0:
        return stack
    if n == 100:
        return stack + ['one', 'hundred']
    if n == 1000:
        return stack + ['one', 'thousand']
    if n in Len:
        return stack + [Len[n]]
    else:
        if n>= 100:
            a, b = divmod(n, 100)
            if b != 0:
                ret = stack+[Len[a]+'hundredand']
            else:
                ret = stack+[Len[a]+'hundred']
            return gen_num(b, stack+ret)
        elif n >= 10:
            a, b = divmod(n, 10)
            return gen_num(b, stack+[Len[a*10]])               

lens = sum(sum(len(j) for j in gen_num(i)) for i in range(1, 1001))
print lens
#a = gen_num(342)
#print a, sum(len(j) for j in a)
        
    
    
