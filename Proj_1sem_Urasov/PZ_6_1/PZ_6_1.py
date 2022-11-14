# Дан целочисленный список размера N. Увеличить все нечетные числа,
# содержащиеся в списке, на исходное значение последнего нечетного числа. Если
# нечетные числа в списке отсутствуют, то оставить список без изменений.


import random #подключение библиотеки
def bbb(v): #Создание вункции
    a = []
    for m in v: #Создание цикла for
        if m % 2 == 1: #условие
            a.append(m) #добавление в список a числа m
    return a #возвращает список a
try: #обработчик исключений
    N=int(input('введите число >>> '))
    a=[]
    y=0
    while y<N: #создание цикла while
       a.append(random.randint(1, 1000)) #Добавление в список a рандомного числа от 1 до 1000
       y+=1
    s=bbb(a) #присваевание переменной функции
    j=len(s) #присваевание переменной значения равному количеству элементов в списке s
    p=0
    if s != []: #условие
       for p in range(j): #Создание цикла for
           s[p]+s[-1] #добавление к элементу под номером p последнего элемента списка
           p+=1
       print(s) 
    else: #выполняется при не соблюдении условия
       print(a)
except ValueError as ve: #исключение
    print('Не целочисленное', ve)
