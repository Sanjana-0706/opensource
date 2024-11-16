n=int(input())
a=list(map(int,input().split()))
s=set()
k=[]
for i in a:
    if i not in s:
        k.append(i)
        s.add(i)
print(*k)
