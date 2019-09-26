dic={1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 100:7, 1000:11, 'and':3}

def numtoEng(num):
    n=0
    result=0
    while n<num:
        n+=1
        if n<=10:
            result+=dic.get(n)
        elif n<100:
            a = n % 10  # 일의 자리
            b = n // 10 % 10  # 십의 자리
            if b==1:
                result+=dic.get(b*10+a)
            else:
                result+=dic.get(b*10)
                if a:
                    result+=dic.get(a)
        elif n<1000:
            a=n%10      # 일의 자리
            b=n//10%10  # 십의 자리
            c=n//100%10 # 백의 자리
            result+=dic.get(c)+dic.get(100)
            if b==1:
                result+=dic.get('and')+dic.get(b*10+a)
            elif b:
                result+=dic.get('and')+dic.get(b*10)
                if a:
                    result+=dic.get(a)
            elif a:
                result+=dic.get('and')+dic.get(a)
        elif n==1000:
            result+=dic.get(1000)
    return result

print(numtoEng(1000))