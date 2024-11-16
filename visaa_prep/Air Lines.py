import math
a,b=map(int,input().split())
c=a*100
d=math.ceil(b/100)
print(max(0,d-a))
