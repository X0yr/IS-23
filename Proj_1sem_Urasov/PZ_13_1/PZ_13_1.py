# Сгенерировать матрицу, в которой нечетные элементы заменяются на 0

import random #заводим библиотеку random
def matrix(): #создаём фунцию с помощью которой сгенирируем матрицу
    stolb = int(input("Введите олличество строк >>>  "))
    strok = int(input("Введите олличество столбцов >>>  "))
    return [[random.randint(10, 20) for i in range(strok)] for j in range(stolb)] #генеируем количество стобцов и строк в матрице при помощи return
b = matrix()
print(b)
c = [[0 if k % 2 != 0 else k for k in i] for i in b] #заносим в список все элементы матрицы b и все нечётные приравниваем к 0
print(c)