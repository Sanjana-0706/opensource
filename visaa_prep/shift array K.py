n=int(input())
a=list(map(int,input().split()))
k=int(input())
k=k%n
m=a[-k:]+a[:-k]
print(*m)
