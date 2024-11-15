x,y,z=map(int,input().split())
c=0
for a in range(1,x):
    if a*y==z:
        c=c+1
if c>=1:
    print("YES")
else:
    print("NO")
