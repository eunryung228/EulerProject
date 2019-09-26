numList=[]
for num in range(100, 1000):
    for num2 in range(100, 1000):
        if len(str(num*num2))%2==0:
              numList.append(num * num2)

best=0
for n in numList:
    a = n % 10
    b = n // 10 % 10
    c = n // 100 % 10
    d = n // pow(10, 3) % 10
    e = n // pow(10, 4) % 10
    f = n // pow(10, 5) % 10
    if a==f and b==e and c==d:
        if best<n: best=n

print(best)