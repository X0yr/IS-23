# Даны целые числа a, b, c, являющиеся сторонами некоторого треугольника.
# Проверить истинность высказывания: «Треугольник со сторонами a, b, c является
# равнобедренным».
try:  #функция проферки
    a = float(input('Введите сторону треугольника ')) #Ввод переменной
    b = float(input('Введите сторону треугольника ')) #Ввод переменной
    c = float(input('Введите сторону треугольника ')) #Ввод переменной
    if a == b and a != c \
            or a == c and a != b \
            or b == c and c != a: #Условие
        print('Треугольник равнобедренный') #Вывод текста
    else: #если не выполняется условие
        print('Треугольник не равнобедренный') #Вывод текста
except: #выполняется если не прохоодит проверку
    print('error') #Вывод текста