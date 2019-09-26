def fibonachi(num):
    if num==0: return 1
    elif num==1: return 2
    else: return fibonachi(num-2)+fibonachi(num-1)

fiblist=[]
for i in range(33):
    fiblist.append(fibonachi(i))

result=0
for arg in fiblist:
    if arg%2==0 and arg<=4000000:result+=arg

print(result)