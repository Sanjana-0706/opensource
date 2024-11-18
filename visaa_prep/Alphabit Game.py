a=input()
c1=0
c2=0
s='aeiouAEIOU'
k='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
for i in a:
    if i in s:
        c1+=1
    if i in k:
        c2+=1
print(f"{c1},{c2}")
