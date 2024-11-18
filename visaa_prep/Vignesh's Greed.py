a=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
for i in range(a-2):
    if l[i]<l[i+1]+l[i+2]:
        print(l[i]+l[i+1]+l[i+2])
        break
else:
    print(-1)
