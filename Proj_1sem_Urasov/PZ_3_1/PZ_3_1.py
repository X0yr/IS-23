try:
    a = float(input('Введите сторону треугольника '))
    b = float(input('Введите сторону треугольника '))
    c = float(input('Введите сторону треугольника '))
    if a == b and b == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник не равнобедренный')
except:
    print('error')