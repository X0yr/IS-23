try:
    a = float(input('введите число '))
    b = float(input('введите число '))
    c = float(input('введите число '))
    if a > c and b > c:
        print(a + b)
    if a > c and c > b:
        print(a + c)
    if c > b and b > a:
        print(b + c)
    if b > a and c > a:
        print(b + c)
    else:
        print('числа равны')
except:
    print('error')