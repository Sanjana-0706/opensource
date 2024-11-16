a,b=map(str,input().split())
if((a=='S' and b=='P') or (a=='P' and b=='R') or (a=='R' and b=='S')):
    print("Vignesh")
elif((a=='S' and b=='S') or (a=='P' and b=='P') or (a=='R' and b=='R')):  
    print("NULL")
else:
    print("Charan")
