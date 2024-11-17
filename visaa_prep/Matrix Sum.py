a=int(input())
l=[list(map(int,input().split())) for _ in range(a)]
rs=[0]*a
cs=[0]*a
for i in range(a):
    for j in range(a):
        rs[i]+=l[i][j]
        cs[j]+=l[i][j]
k=[]
for i in range(a):
    k.append(rs[i]+cs[i])
print(" ".join(map(str,k)))
