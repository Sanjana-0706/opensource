a=input()
l=len(a)
r=""
c=1
for i in range(1,l):
    if a[i]==a[i-1]:
        c+=1
    else:
        r+=a[i-1]+str(c)
        c=1
r+=a[-1]+str(c)
print(r)
