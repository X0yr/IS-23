import random
try:
    a=[]
    j=int(input('Введите число >>> '))
    u=1
    while u<j: #цикл, работающий пока переменная u меньше переменной j
        a.append(random.randint(1, 100)) #добовление рандомного числа в диапазоне от 1 до 100 в конец списка
        u+=1
    a.sort() #Сортировка элементов в списке, от меньшего к большему
    a.append(random.randint(1, 100)) #добовление рандомного числа в диапазоне от 1 до 100 в конец списка
    a.sort() #Сортировка элементов в списке, от меньшего к большему
    print(a)
except:
    print('Error')