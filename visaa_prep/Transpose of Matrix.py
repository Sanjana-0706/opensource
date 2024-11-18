n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
t=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        t[i][j]=a[j][i]
for i in t:
    print(' '.join(map(str,i)))
