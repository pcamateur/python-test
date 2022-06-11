la = [a1 for a1 in 'abcd']
lb = [str('a'+str(b2)) for b2 in range(len(la))]
lc = [str('b'+str(c2)) for c2 in range(len(la))]
ld = [str('c'+str(d2)) for d2 in range(len(la))]
le = [str('d'+str(e2)) for e2 in range(len(la))]
lf = []
print(la,'\n',lb,'\n',lc,'\n',ld,'\n',le)
# lis = [str('a') for x in range(len(lb))]
# print(lis)
# s1 = dict(zip(lis,lb))
# print(s1)
lis = list()
for x in range(len(lb)):
    lis.append({la[0]:lb[x],la[1]:lc[x],la[2]:ld[x],la[3]:le[x]})
print(lis)