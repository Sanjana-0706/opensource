N=int(input())
for i in range(0,N):
    x,y=map(int,input().split())
    if x<=y:
        print("0")
    else:
        print(x-y)
