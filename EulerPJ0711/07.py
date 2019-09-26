import math

def primeNum(num):
    if num==1:
        return 2
    elif num==2:
        return 3
    elif num==3:
        return 5
    elif num==4:
        return 7
    n=10
    pnum=4
    while True:
        for i in range(2, int(math.sqrt(n))+1):
            if n%i==0:
                break
            if i==int(math.sqrt(n)):
                pnum+=1
        if pnum==num:
            return n
        n+=1

print(primeNum(10001))