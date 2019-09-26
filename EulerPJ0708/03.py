x=600851475143
d=2

while d<=x:
    if x%d==0:
        print(d, end=" ")
        x=x/d
    else:
        d+=1