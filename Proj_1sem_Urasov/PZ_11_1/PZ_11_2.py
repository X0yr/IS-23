# Из предложенного текстового файла (text18-31.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить строку наименьшей длины.

fil = open('text18-31.txt', encoding='UTF-8')

print(fil.read())

mylist = fil.readlines()
print(mylist)

# data = fil.read().replace(" ", "")
# number_of_charecters = len(data)
# print(number_of_charecters)
# fil.close()