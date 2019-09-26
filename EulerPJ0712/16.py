def sum_digit(num):
    result=0
    for i in str(num):
        result+=int(i)
    return result

print(sum_digit(pow(2, 1000)))