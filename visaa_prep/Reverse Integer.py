n=int(input())
s=-1 if n<0 else 1
n=abs(n)
r=int(str(n)[::-1])
if r>2**31-1 or r<-2**31:
    print(0)
else:
    print(s*r)
