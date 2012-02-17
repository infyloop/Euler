lst = [a**b for a in range(2, 101) for b in range(2, 101)]
present = []
for i in lst:
    if not i in present:
    present.append(i)
print len(present)

