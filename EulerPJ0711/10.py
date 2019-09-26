import math

def primeNum(num):
    n=2
    sum=0
    while n<=num:
        if n==2 or n==3:
            sum+=n
        for i in range(2, int(math.sqrt(n))+1):
            if n%i==0:
                break
            if i==int(math.sqrt(n)):
                sum += n
        n+=1
    return sum

print(primeNum(2000000))