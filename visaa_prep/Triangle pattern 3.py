a=int(input())
for i in range(1,a+1):
    for j in range(i):
        print(j+1,end="")
    for j in range(2*(a-i)):
        print(" ",end="")
    for j in range(i):
        print(i-j,end="")
    print()
