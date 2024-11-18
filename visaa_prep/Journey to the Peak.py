a=int(input())
l=list(map(int,input().split()))
ma=0
ca=0
for i in l:
    ca+=i
    ma=max(ca,ma)
print(ma)
