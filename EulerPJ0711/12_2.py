def GetDivnum(trinum):
    num=0
    temp=trinum
    div2num=0
    mulodd=1

    if trinum==1: return 1

    while temp%2==0:
        temp=temp//2
        div2num+=1

    k = 1
    while temp>1:
        k += 2
        divoddnum=0
        while temp % k == 0:
            temp = temp // k
            divoddnum += 1
        if divoddnum:
            mulodd = mulodd * (divoddnum + 1)
            num=(div2num+1)*mulodd
    return num

n=1
while True:
    trinum=n*(n+1)//2
    if GetDivnum(trinum)>=500:
        print(trinum)
        break
    n+=1