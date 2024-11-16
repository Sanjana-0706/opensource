a=int(input())
l=list(map(int,input().split()))
r=l[1:]+l[:1]
print(*r)
