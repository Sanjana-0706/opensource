n,m=map(int,input().split())
mat=[]
for i in range(n):
    x=list(map(int,input().split()))
    mat.append(x)
row,col=[],[]
for i in range(n):
    for j in range(m):
        if mat[i][j]==0:
            row.append(i)
            col.append(j)
for i in range(n):
    for j in range(m):
        if i in row or j in col:
            mat[i][j]=0
for i in range(n):
    for j in range(m):
        print(mat[i][j],end=' ')
    print()
