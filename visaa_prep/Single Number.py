a=int(input())
k=list(map(int,input().split()))
c=0
for i in k:
    c^=i
print(c)
