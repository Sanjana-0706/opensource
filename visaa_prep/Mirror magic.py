n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
for i in a:
    print(" ".join(map(str,i[::-1])))
