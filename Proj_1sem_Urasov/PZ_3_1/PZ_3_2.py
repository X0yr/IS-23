# Даны три числа. Найти сумму двух наибольших из них.
try: #функция проферки
    a = float(input('введите число ')) #Ввод переменной
    b = float(input('введите число ')) #Ввод переменной
    c = float(input('введите число ')) #Ввод переменной
    if a > c and b > c: #Условие
        print(a + b) #Вывод суммы
    if a > c and c > b: #Условие
        print(a + c) #Вывод суммы
    if c > b and b > a: #Условие
        print(b + c) #Вывод суммы
    if b > a and c > a: #Условие
        print(b + c) #Вывод суммы
    else: #если не выполняется условие
        print('числа равны')
except: #выполняется если не прохоодит проверку
    print('error') #Вывод текста
