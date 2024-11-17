n,d=map(int,input().split())
a=list(map(int,input().split()))
l1=[]
l2=[]
for i in a:
    if i%d==0:
        l1.append(i)
    else:
        l2.append(i)
print(sum(l1)-sum(l2))
