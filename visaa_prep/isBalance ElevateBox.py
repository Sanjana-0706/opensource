n=int(input())
a=list(map(int,input().split()))
s=[]
for i in range(n):
    sum1=sum(a[0:i])
    sum2=sum(a[i+1:])
    s.append(abs(sum1-sum2))
print(' '.join(map(str,s)))
