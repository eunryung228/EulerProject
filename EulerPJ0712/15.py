from math import factorial

def road_num(row, col):
    return factorial(row+col)//(factorial(row)*factorial(col))

a, b=input("격자의 사이즈를 입력해주세요: ").split()
a=int(a)
b=int(b)

print(road_num(a, b))