def collatz(num):
    count=1
    temp=num
    while temp!=1:
        if temp%2==0:
            temp=temp//2
            count+=1
        elif temp%2==1:
            temp=3*temp+1
            count+=1
    return count

n=0
best=0
bestnum=0
while n<=1000000:
   n+=1
   if collatz(n)>best:
       best=collatz(n)
       bestnum=n

print(bestnum)