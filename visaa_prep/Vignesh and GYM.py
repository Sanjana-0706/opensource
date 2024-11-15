m,n,o=map(int,input().split())
if m+n<=o:
    print("2")
else:
    if m<=o:
        print("1")
    else:
        print("0")
