# Найти сумму чисел ряда 1,2,3,...,60 с использованием функции нахождения суммы.
# Использовать локальные переменные.
try: #обработчик исключений
    a=[] #создаём пустой список
    B=0 #присваивание переменной чесло
    while B<=60: #создаём цикл
        a.append(B) #прибавление к переменной 1
        B=B+1 #присваивание переменной итог выражения
    v=sum(a) #присваеваем переменой сумму элементов списка
    print(v) #выводим сумму элементов списка
except: #работает при нахождении исключений
    print("Error")