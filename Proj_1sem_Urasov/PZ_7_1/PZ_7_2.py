# Дана строка, состоящая из русских слов, разделенных пробелами (одним или
# несколькими). Найти длину самого короткого слова.

import re


# stroca_1 = "Дана строка тоясосщая из русских слов разделенных пробелами."
# print(min(re.findall(r'[а-яА-ЯёЁ]+', stroca_1)[::-1], key=len)) #с помошью функции re.findall перебираем все
#                                                                 # слова с заданным алфавилом в стоке и выводим минимальноее


stroca_1 = "Дана строка состоящая из русских слов разделенных пробелами."
v = 0
x = 0
c = 0
my_sp = [] #список в который мы внесём длинну каждого слова
while v <= len(stroca_1): #цикл работающий пока переменная v меньше чем длинна строки
    if stroca_1[c:c+1] == ' ' or stroca_1[c:c+1] == '.' or stroca_1[c:c+1] == ',': #условие выполняющееся если при переборе элементов строки
        my_sp.append(len(stroca_1[x:c]))                                           #мы встечает точку, пробел или запятую
        x = c+1
    c += 1
    v += 1
print(my_sp) #выведем исходный список
print(min(my_sp)) #выведем длинну самого маленького слова