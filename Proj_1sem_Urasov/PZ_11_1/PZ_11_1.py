# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Элементы первого и второго файлов:
# Количество элементов первого и второго файлов:
# Элементы первой трети:
# Минимальный элемент первой трети:
import  random
list1 = [random.randint(-30, 30) for i in range(random.randint(10, 30))]
list2 = [random.randint(-30, 30) for i in range(random.randint(10, 30))]

list3 = list1+list2
a= len(list3)//3
print(a)
elem = list3[0:a]


list1=str(list1)
list2=str(list2)



fl1 = open('my_file1.txt', 'w', encoding='UTF-8')
fl2 = open('my_file2.txt', 'w', encoding='UTF-8')
fl3 = open('my_file3.txt', 'w', encoding='UTF-8')

a= len(list3)//3
elem = list3[0:a]
print(elem)


fl1.write(f"Содержимое: {list1}")
fl2.write(f"Содержимое: {list2}")
fl3.write(f"Содержимое: {list3}\n")
fl3.write(f"Количество элементов: {len(list3)}\n")
fl3.write(f"Элементы первой трети: {elem}\n")
fl3.write(f"Минимальный элемент первой трети: {min(elem)}")





fl1.close()
fl2.close()
fl3.close()
