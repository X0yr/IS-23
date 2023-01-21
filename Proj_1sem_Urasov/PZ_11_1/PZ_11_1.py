# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Элементы первого и второго файлов:
# Количество элементов первого и второго файлов:
# Элементы первой трети:
# Минимальный элемент первой трети:
import  random
list1 = [random.randint(-30, 30) for i in range(random.randint(10, 30))] #Будущее содержимое файла my_file1.txt
list2 = [random.randint(-30, 30) for i in range(random.randint(10, 30))] #Будущее содержимое файла my_file2.txt

list3 = list1+list2 #Складываем содержимое list1 и list2
a= len(list3)//3 #считаем колличество первой трети
# print(a)
elem = list3[0:a] #заносим в новый лист элементы первой трети list3


list1=str(list1)
list2=str(list2)



fl1 = open('my_file1.txt', 'w', encoding='UTF-8') #открываем файл my_file1.txt
fl2 = open('my_file2.txt', 'w', encoding='UTF-8') #открываем файл my_file2.txt
fl3 = open('my_file3.txt', 'w', encoding='UTF-8') #открываем файл my_file3.txt




fl1.write(f"Содержимое: {list1}") #заносим в файл содержимое list1
fl2.write(f"Содержимое: {list2}") #заносим в файл содержимое list2
fl3.write(f"Содержимое: {list3}\n") #заносим в файл содержимое list3
fl3.write(f"Количество элементов: {len(list3)}\n") #заносим в файл количеслво элементов в list3
fl3.write(f"Элементы первой трети: {elem}\n") #заносим в файл элементы первой трети листа list3
fl3.write(f"Минимальный элемент первой трети: {min(elem)}") #заносим в файл минимальный элемент листа list3





fl1.close()
fl2.close()
fl3.close()
