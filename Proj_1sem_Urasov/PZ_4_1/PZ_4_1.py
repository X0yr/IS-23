# Дано вещественное число A и целое число N (>0). Найти A в степени N: AN = AA ...
# •A (числа A перемножаются N раз).
try: #функция проферки
    A=float(input('Введите число >')) #Ввод переменной
    N=int(input('Введите степень числа >')) #Ввод переменной
    B=A**N #Посчет и занесение полученного числа в переменную
    print(B) #Вывод переменной
except: #выполняется если не прохоодит проверку
    print('error')  #Вывод текста