stroca_1 = "Дана строка состоящая из русских слов разделенных пробелами"
list_1 = stroca_1.split(" ")
myList_1 = 0
for i in range(len(list_1)):
    if len(list_1[i]) < len(list_1[myList_1]):
        print(list_1[i])