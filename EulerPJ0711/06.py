sum=0
for i in range(1, 101):
    sum+=i

sumofpow=0
for i in range(1, 101):
    sumofpow+=i*i

print(pow(sum,2)-sumofpow)