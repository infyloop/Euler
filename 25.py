maxi = int('1%s' % ('0' * 999))
st1 = 0
st2 = 1
cnt = 1
while(len(str(st2))<=999):
    curr, st1 = st1+st2, st2
    st2 = curr
    cnt += 1

print cnt, len(str(st2))
