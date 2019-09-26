from math import sqrt

end = 2000000
test = list(range(0,end+1))
test[0] = test[1] = 0

def is_prime(num):
    if num is 2 or 3 : return True
    for i in range(2,int(sqrt(num)+1)):
        if num%i==0 : return False
    return True

for i  in test:
    if i is 0 : continue
    if is_prime(i):
        for j in range(i*2,end+1,i):
            test[j] = 0
print(sum(test))