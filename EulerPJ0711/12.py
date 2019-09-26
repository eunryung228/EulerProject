from math import sqrt

trinumList=[]
for n in range(46, 30000):
    sum = 0
    for a in range(1, n):
        sum += a
    trinumList.append(sum)

def Getdivisor(numList):
    divList=[]
    for argnum in range(len(numList)):
        num=numList[argnum]
        div = []
        for s in range(1, int(sqrt(num)+1)):
            if num%s==0:
                div.append(s)
                div.append(num//s)
        divList.append(sorted(div))
        argnum+=1
    return divList

getList=Getdivisor(trinumList)

for i in range(len(getList)):
    if len(getList[i])>=500:
        print(getList[i][-1], end=" ")
