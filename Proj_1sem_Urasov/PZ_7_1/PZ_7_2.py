import re


stroca_1 = "Дана строка состоящая из русских слов разделенных пробелами"
print(min(re.findall(r'[а-яА-ЯёЁ]+', stroca_1)[::-1], key=len)) #с помошью функции re.findall перебираем все
                                                                # слова с заданным алфавилом в стоке и выводим минимальное

# list_1 = stroca_1.split(" ")
# myList_1 = 0
# for i in range(len(list_1)):
#     if len(list_1[i]) <= len(list_1[myList_1]):
#         print(list_1[i])
#         break