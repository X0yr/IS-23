# Из исходного текстового файла (price.txt) выбрать все цены. Посчитать количество
# полученных элементов.

import re

price = open("price.txt", "r", encoding="UTF-8") #открытие файла на чтение
text = price.read() #с помощью read считываем весь файл

itog = re.findall(r'\d+\sруб\.\s\d+\sкоп\.', text) #re.findall находит все нужные элементы
s = list(set(itog)) #заносим все найденные элементы в list
print(s)

print("Количество элементов", len(s)) #подсчитываем элеметы

price.close()

