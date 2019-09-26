def GetNum(num):
    while True:
        num += 1
        for i in range(2, 21):
            if num % i != 0:
                break
            if i == 20:
                return num

print(GetNum(0))